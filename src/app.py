# This will be the entry point for the application
import argparse
import os


def main():
    """
    This will be the entry point for the application
    access the command line arguments
    --filepath: path to the file containing the URLs
    --output_dir: path to the output directory
    --batch_size: number of concurrent downloads
    :return:
    """
    parser = argparse.ArgumentParser(description='Download images from a list of URLs')
    parser.add_argument('--filepath', required=True,
                        help='Path to file containing URLs, path can be absolute or relative')
    parser.add_argument('--output_dir', required=False,
                        help='Path to output directory, path can be absolute or relative')
    parser.add_argument('--batch_size', type=int, default=100, help='Number of concurrent downloads')
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)



if __name__ == "__main__":
    main()
