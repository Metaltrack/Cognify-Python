import os
import shutil

def Organize():
    path = input("Enter folder path: ").strip("\"'")

    extensions = {

        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Code": [".py", ".cpp", ".java", ".c", ".js", ".glsl", ".gd", ".cs"],
        "Assets": [".gltf", ".glb", ".fbx", ".obj"],
        "Sound": [".ogg", ".mp3"]
    }

    report=[]

    for file in os.listdir(path):

        full_path=os.path.join(path,file)

        if os.path.isfile(full_path):

            moved=False

            for folder,exts in extensions.items():

                if any(file.lower().endswith(ext)
                       for ext in exts):

                    destination=os.path.join(
                        path,
                        folder
                    )

                    os.makedirs(
                        destination,
                        exist_ok=True
                    )

                    shutil.move(
                        full_path,
                        os.path.join(
                            destination,
                            file
                        )
                    )

                    report.append(
                        f"{file} -> {folder}"
                    )

                    moved=True
                    break

            if not moved:

                other=os.path.join(
                    path,
                    "Others"
                )

                os.makedirs(
                    other,
                    exist_ok=True
                )

                shutil.move(
                    full_path,
                    os.path.join(
                        other,
                        file
                    )
                )

                report.append(
                    f"{file} -> Others"
                )

    # Generate report
    with open(
        os.path.join(path,"report.txt"),
        "w"
    ) as f:

        f.write(
            "\n".join(report)
        )

    print("Done. also report created")

if __name__ == "__main__":
    while(True):
        print("""Level 3 Automation...
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            Organize()
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
