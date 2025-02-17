# Stable Diffusion WebUI Pillow Patch

This extension for Stable Diffusion WebUI addresses compatibility issues with newer versions of the Pillow library. Specifically, it provides a patch for the missing `multiline_textsize` function by using a wrapper method that delegates to Pillow's `textlength` method.

## Features

- Patches the missing `multiline_textsize` function in newer Pillow versions.
- Uses a wrapper method to delegate to Pillow's `textlength` method.

## Installation

1. Clone this repository into your Stable Diffusion WebUI extensions directory:
    ```sh
    git clone https://github.com/MisterChief95/sd-webui-pillow-patch.git
    ```
2. Restart your Stable Diffusion WebUI.

## Usage

The patch is applied automatically when the extension is loaded. No additional configuration is required.

## License

This project is licensed under the Apache 2 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
