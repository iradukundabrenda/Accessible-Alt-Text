"""
alt_text_generator.py

This module contains functions to generate descriptive alternative text (alt text) for images.
"""

def clean_image_url(url):
    """
    Clean and validate the image URL string.

    Args:
        url (str): The raw image URL.

    Returns:
        str: The cleaned URL if valid, else an empty string.
    """
    if not url or not isinstance(url, str):
        return ""
    url = url.strip()
    if url.startswith("http"):
        return url
    return ""

def generate_alt_text(image_url):
    """
    Generate descriptive alt text for the given image URL.

    Args:
        image_url (str): The URL of the image to describe.

    Returns:
        str: A descriptive alt text string.
    """
    clean_url = clean_image_url(image_url)
    if not clean_url:
        return "Invalid image URL provided."
    return "This is a placeholder alt text for the image."


