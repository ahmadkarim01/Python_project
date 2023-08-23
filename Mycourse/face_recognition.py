from unittest import result
import face_recognition

ahmad=face_recognition.load_image_file("ah1.jpg")
ahmad_encoding=face_recognition.face_encodings(ahmad)[0]

unknown_image=face_recognition.load_image_file("ah2.jpg")
unknown_image_enconding=face_recognition.face_encodings(unknown_image)[0]

result=face_recognition.compare_faces([ahmad_encoding],unknown_image)