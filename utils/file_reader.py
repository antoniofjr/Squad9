import pandas as pd
import xml.etree.ElementTree as ET
import traceback


def read_file(file_path):

    try:

        # =========================
        # CSV
        # =========================
        if file_path.endswith(".csv"):

            df = pd.read_csv(file_path)

            print("\nCSV carregado com sucesso")
            print(df.head())

            return df

        # =========================
        # XML
        # =========================
        elif file_path.endswith(".xml"):

            # abre XML manualmente
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                xml_content = f.read()

            root = ET.fromstring(xml_content)

            data = []

            for elem in root.iter():

                row = {
                    "tag": str(elem.tag),
                    "text": str(elem.text).strip() if elem.text else ""
                }

                # adiciona atributos
                for key, value in elem.attrib.items():
                    row[key] = value

                data.append(row)

            df = pd.DataFrame(data)

            print("\nXML carregado com sucesso")
            print(df.head())

            return df

        else:

            print("Formato não suportado")
            return None

    except Exception as e:

        print("\n========== ERRO COMPLETO ==========")

        traceback.print_exc()

        print("===================================")

        return None