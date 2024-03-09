from flask import render_template, abort, request

from aplicacao.models import Animais
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
# from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50

model = ResNet50()


def init_app(app):
    @app.route("/")
    def index():
        animais = Animais.query.all()
        return render_template("index.html", animais=animais)

    @app.route("/animal/<animal_id>")
    def animal(animal_id):
        animais = Animais.query.filter_by(id=animal_id).first() or abort(
            404, "Animal não encontrado"
        )
        return render_template("product.html", animal=animais)

    @app.route("/", methods=['GET'])
    def imagens():
        return render_template("images.html")

    @app.route("/", methods=['POST'])
    def predict():
        imagefile = request.files['imagefile']
        image_path = "./images/" + imagefile.filename
        imagefile.save(image_path)

        image = load_img(image_path, target_size=(224, 224))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        yhat = model.predict(image)
        label = decode_predictions(yhat)
        label = label[0][0]

        classification = '%s (%.2f%%)' % (label[1], label[2] * 100)

        return render_template('images.html', prediction=classification)

    if __name__ == "__main__":
        app.run(port=3000, debug=True)
