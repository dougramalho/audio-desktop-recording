import argparse
import src.start as console

def execute():
    console.main()


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Comunidade de agentes")

    execute()
    # parser.add_argument("tool", choices=["lab"], help="Agentes disponíveis: lab")

    # args = parser.parse_args()

    # execute(args.tool)