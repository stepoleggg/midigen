from keras.models import model_from_json

def save_model_json(model, file_name):
    model_json = model.to_json()
    file = open(file_name, 'w')
    file.write(model_json)
    file.close()
    return print(f"Succes, file: {file_name}, saved")

def save_weights_h5(model,file_name):
    model.save_weights(file_name)
    return print(f"Succes, file: {file_name}, saved")

def load_model_from_json(file_name):
    json_file = open(file_name, "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    print(f"Succes! Loaded form: {file_name} and returned")
    return loaded_model

def load_weights_h5(file_name, loaded_model):
    loaded_model.load_weights(file_name)
    return loaded_model