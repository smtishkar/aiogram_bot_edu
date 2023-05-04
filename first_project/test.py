arr_photos = ["https://yandex.ru/images/search?pos=40&img_url=https%3A%2F%2Fsun9-9.userapi.com%2Fimpg%2FU8DJ2JiZtnRCMyufsqGVeaCoEnrI3zt6OwfOBA%2F4XbMeBkLWXk.jpg%3Fsize%3D800x527%26quality%3D96%26sign%3D1c2c9c269893d023bee6aba85787d9a4%26c_uniq_tag%3DlxQMy7HkDGAKV4NrWRpkdoXesyGRinlPJDqMHcxpG6Q%26type%3Dalbum&text=коты+смешные&rpt=simage&lr=213",
              "https://yandex.ru/images/search?p=1&text=коты+смешные&pos=34&rpt=simage&img_url=https%3A%2F%2Fimg1.goodfon.ru%2Foriginal%2F5184x3456%2Fb%2F72%2Fskottish-fold-morda-shapka.jpg&lr=213",
              "https://yandex.ru/images/search?p=2&text=коты+смешные&pos=26&rpt=simage&img_url=https%3A%2F%2Fkrasivosti.pro%2Fuploads%2Fposts%2F2021-03%2F1616466037_28-p-tri-kota-i-koshechka-foto-koshka-34.jpg&lr=213"]

photos = dict(zip(arr_photos, ['1', '2', '3']))             #zip - чтобы сшить два массива в одном словаре

print(photos)