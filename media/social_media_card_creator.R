magick::image_read("media/logos_combined.jpeg") |>
  magick::image_resize(geometry = "1280x640") |>
  magick::image_write(path = "media/social-media-card.png")
