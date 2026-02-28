import os
from PIL import Image

def add_surprised_pikachu(input_path, output_path=None, overlay_path='pikachu.png', margin_ratio=0.02, max_overlay_width_ratio=0.2):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '_pikachu.png'

    # Open base image and ensure RGBA mode
    base = Image.open(input_path).convert('RGBA')

    # Open overlay (Pikachu face) and ensure RGBA mode
    overlay = Image.open(overlay_path).convert('RGBA')

    # Scale overlay to at most max_overlay_width_ratio of base width
    max_overlay_width = int(base.width * max_overlay_width_ratio)
    if overlay.width > max_overlay_width:
        new_height = int(overlay.height * (max_overlay_width / overlay.width))
        overlay = overlay.resize((max_overlay_width, new_height), Image.LANCZOS)

    # Determine position: bottom‑right corner with margin
    x = base.width - overlay.width - int(base.width * margin_ratio)
    y = base.height - overlay.height - int(base.height * margin_ratio)
    if x < 0: x = 0
    if y < 0: y = 0

    # Paste overlay onto base respecting its alpha channel
    base.paste(overlay, (x, y), overlay)

    # Save result
    base.save(output_path, format='PNG')
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Add a surprised Pikachu reaction overlay to an image.')
    parser.add_argument('input', help='Path to the input image')
    parser.add_argument('-o', '--output', help='Path to output image (default: input_basename_pikachu.png)')
    parser.add_argument('--overlay', default='pikachu.png', help='Path to the Pikachu overlay PNG (default: pikachu.png)')
    parser.add_argument('--margin', type=float, default=0.02, help='Margin as a fraction of base dimensions (default: 0.02)')
    parser.add_argument('--max-width-ratio', type=float, default=0.2, help='Maximum overlay width as a fraction of base width (default: 0.2)')
    args = parser.parse_args()

    add_surprised_pikachu(
        input_path=args.input,
        output_path=args.output,
        overlay_path=args.overlay,
        margin_ratio=args.margin,
        max_overlay_width_ratio=args.max_width_ratio
    )

if __name__ == '__main__':