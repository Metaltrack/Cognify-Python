import pandas as pd
import plotly.express as px
import os

default_path = os.path.dirname(os.path.realpath(__file__)) + "\Formula1_2025Season_RaceResults.csv"

def plot():
    file_path = input("Enter CSV file path (press enter to use default data): ")
    if file_path:
        df = pd.read_csv(file_path)
    else:
        df = pd.read_csv(default_path)

    print("\nDataset Preview:")
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())


    numeric_cols = df.select_dtypes(
        include=['number']
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        include=['object']
    ).columns.tolist()

    print("\nNumeric columns:")
    print(numeric_cols)

    print("\nCategorical columns:")
    print(categorical_cols)


    print("\nSuggested plots:")

    if len(numeric_cols) >= 2:
        print("1. Scatter Plot")

    if len(categorical_cols) >= 1 and len(numeric_cols) >= 1:
        print("2. Bar Chart")

    if len(numeric_cols) >= 1:
        print("3. Histogram")

    print("4. Line Chart")


    choice = input(
        "\nChoose chart type (Enter Number): "
    )

    x = input("Choose X-axis column (choose a column from the cagtegories): ")
    y = None

    if choice != "3":
        y = input(
            "Choose Y-axis column (choose a column from the cagtegories): "
        )

    if choice == "1":
        fig = px.scatter(
            df,
            x=x,
            y=y,
            title=f"{y} vs {x}"
        )
    elif choice == "2":
        fig = px.bar(
            df,
            x=x,
            y=y,
            title=f"{y} by {x}"
        )
    elif choice == "3":
        fig = px.histogram(
            df,
            x=x,
            title=f"Distribution of {x}"
        )
    else:
        fig = px.line(
            df,
            x=x,
            y=y,
            title=f"{y} over {x}"
        )
    fig.show()


if __name__ == "__main__":
    while(True):
        print("""Level 3 DataPlotting...
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            plot()
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
