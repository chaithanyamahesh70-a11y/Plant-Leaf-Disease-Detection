from flask import Flask, render_template, request
import os
import torch
import pandas as pd
from torchvision import transforms
from PIL import Image
from CNN import CNN, idx_to_classes

app = Flask(__name__)

# -----------------------------
# Load Disease CSV
# -----------------------------

disease_data = pd.read_csv(
    "disease_info.csv",
    encoding="latin1"
)

# -----------------------------
# Load Model
# -----------------------------

device = torch.device("cpu")

model = CNN(39)

model.load_state_dict(
    torch.load(
        "plant_disease_model_1_latest.pt",
        map_location=device
    )
)

model.eval()

# -----------------------------
# Image Transform
# -----------------------------

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

# -----------------------------
# Upload Folder
# -----------------------------

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# -----------------------------
# Home
# -----------------------------

@app.route("/")
def home():

    return render_template(
        "home.html"
    )


# -----------------------------
# Detect
# -----------------------------

@app.route("/detect")
def detect():

    return render_template(
        "detect.html"
    )


# -----------------------------
# Contact
# -----------------------------

@app.route("/contact")
def contact():

    return render_template(
        "contact.html"
    )


# -----------------------------
# Predict
# -----------------------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    if "image" not in request.files:

        return "No Image Selected"

    file = request.files["image"]

    if file.filename == "":

        return "No Image Selected"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    image = Image.open(
        filepath
    ).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence = probabilities.max().item() * 100

        predicted = torch.argmax(
            output,
            dim=1
        ).item()

    disease = idx_to_classes[predicted]

    confidence = f"{confidence:.2f}%"
        # -----------------------------
    # Default Values
    # -----------------------------

    treatment = "Consult your nearest Agriculture Officer."

    fertilizer = "Apply balanced NPK fertilizer."

    prevention = "Inspect your crop regularly."

    description = "No additional information available."

    # -----------------------------
    # Convert Disease Name
    # -----------------------------

    search_name = disease

    search_name = search_name.replace(
        "___",
        " : "
    )

    search_name = search_name.replace(
        "_",
        " "
    )

    # -----------------------------
    # Search CSV
    # -----------------------------

    result = disease_data[
        disease_data["disease_name"]
        .astype(str)
        .str.lower()
        .str.contains(
            search_name.lower(),
            na=False
        )
    ]

    if not result.empty:

        if pd.notna(
            result.iloc[0]["description"]
        ):
            description = str(
                result.iloc[0]["description"]
            )

        if pd.notna(
            result.iloc[0]["Possible Steps"]
        ):
            treatment = str(
                result.iloc[0]["Possible Steps"]
            )

        fertilizer = (
            "Apply fertilizer according "
            "to soil test and crop stage."
        )

        prevention = (
            "Use disease-free seeds, "
            "maintain field hygiene, "
            "avoid overwatering and "
            "inspect plants regularly."
        )

    return render_template(

        "result.html",

        image=file.filename,

        disease=disease.replace(
            "___",
            " : "
        ).replace(
            "_",
            " "
        ),

        confidence=confidence,

        description=description,

        treatment=treatment,

        fertilizer=fertilizer,

        prevention=prevention

    )


# -----------------------------
# Run Flask
# -----------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )