"""Output a QR code with specific formatting."""

import qrcode


def make_qr_code(
    image_name: str,
    image_fill_colour: str,
    image_back_colour: str,
    qr_value: str,
):
    """
    Output a QR code with specific formatting.

    Parameters
    ----------
    image_name : str
        The name of the QR code to save.
    image_fill_colour : str
        The colour of the QR code foreground.
    image_back_colour : str
        The colour of the QR code background.
    """
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1,
    )

    qr.add_data(qr_value)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color=image_fill_colour,
        back_color=image_back_colour,
    )

    image.save(image_name)


make_qr_code("Test.png", "Green", "White", "www.google.com")
