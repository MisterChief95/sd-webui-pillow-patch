from PIL import ImageDraw

if hasattr(ImageDraw.Draw, 'multiline_textsize'):
    print("ImageDraw.Draw does not required patching")

else:
    print("ImageDraw.Draw missing multiline_textsize, patching... ", end='')

    # Save the original Draw function
    original_Draw = ImageDraw.Draw

    def monkey_patch(self, text, font=None, *args, **kwargs):
        # Adds a small space to the text for padding
        longest_line: str = max(text.split('\n'), key=len)
        return (self.textlength(longest_line + "  ", font=font),)


    def Draw(im, mode=None):
        # Call the original Draw function
        d = original_Draw(im, mode)
        
        # Apply the monkey patch
        if not hasattr(d, 'multiline_textsize'):
            d.multiline_textsize = monkey_patch.__get__(d, ImageDraw)
        
        return d

    # Replace the original Draw function with the patched one
    ImageDraw.Draw = Draw

    print("Patched!")
