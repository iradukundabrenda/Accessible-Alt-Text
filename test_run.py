from alt_text_generator import generate_alt_text

test_url_good = "http://example.com/image.jpg"
test_url_bad = "ftp://badurl.com/image.jpg"
test_url_empty = ""

print(generate_alt_text(test_url_good))   # Should print placeholder alt text
print(generate_alt_text(test_url_bad))    # Should print "Invalid image URL provided."
print(generate_alt_text(test_url_empty))  # Should print "Invalid image URL provided."

