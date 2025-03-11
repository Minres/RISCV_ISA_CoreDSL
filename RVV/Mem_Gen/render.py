import argparse
import sys

from jinja2 import Environment, FileSystemLoader


def render_template(template_path, context):
    env = Environment(
        loader=FileSystemLoader(".")
    )  # Load templates from the current directory
    template = env.get_template(template_path)
    return template.render(context)


def main():
    parser = argparse.ArgumentParser(description="Render a Jinja template ")
    parser.add_argument("template", help="Path to the Jinja template file.")
    args = parser.parse_args()
    segment_data = {
        "size": [1, 2, 3, 4, 5, 6, 7, 8],
        "bits": ["000", "001", "010", "011", "100", "101", "110", "111"],
    }
    elem_data = {"size": [8, 16, 32, 64], "bits": ["000", "101", "110", "111"]}

    context = {}
    for s_idx in range(len(segment_data["bits"])):
        for e_idx in range(len(elem_data["bits"])):
            context = {
                "segment_size": segment_data["size"][s_idx],
                "segment_bits": segment_data["bits"][s_idx],
                "elem_size": elem_data["size"][e_idx],
                "elem_bits": elem_data["bits"][e_idx],
            }
            try:
                output = render_template(args.template, context)
                if output:
                    print(output)
            except Exception as e:
                print(f"Error rendering template: {e}", file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
