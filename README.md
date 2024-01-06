# Instagram Profile Picture Downloader

This Python application allows you to easily download Instagram profile pictures without the need for login credentials or the use of Selenium. Simply call the `get_profile_pic` function with the Instagram username as an argument, and the profile picture will be downloaded.

## Usage

1. Ensure you have Python installed on your machine.

2. Clone this repository or download the `insta_profile_pic_downloader.py` file.

3. Install the required dependencies using the following command:

    ```bash
    pip install requests
    ```

4. Use the `get_profile_pic` function in your Python script or interactive environment:

    ```python
    from insta_profile_pic_downloader import get_profile_pic

    # Replace 'username' with the desired Instagram username
    get_profile_pic('username')
    ```

5. Run your Python script, and the profile picture will be downloaded and saved in the current working directory.

## Important Notes

- This application does not require any login credentials.

- It does not use Selenium or any other automated browser tool.

- The downloaded profile picture will be saved in the current working directory with the filename format: `username_profile_pic.jpg`.

## Disclaimer

This application is for educational and personal use only. Respect Instagram's terms of service and the privacy of other users while using this tool.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and enhancements are welcomed!
