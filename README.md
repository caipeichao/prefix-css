prefix-css
==========

Tools for prefixing all css classes.

# Usage
Download prefixcss.py and run command:

    python prefixcss.py mystyle.css .myprefix > newstyle.css

For a css file mystyle.css:

    .button { background-color: #f00; }
        
Will get newstyle.css:

    .myprefix .button { background-color: #f00; }
        
# Why to use?
I want to mix Bootstrap and Foundation. This tool can avoid conflictions. 

With prefixed stylesheets, you can mix two css in this way:

    <foundation>
        <div class="button">Hello</div>
        <div class="progress large-6 round success">
            <span class="meter" style="width: 60%;"></span>
        </div>
    </foundation>
    <bootstrap>
        <div class="btn">World!</div>
        <div class="progress">
            <div class="bar" style="width: 60%;"></div>
        </div>
    </bootstrap>

For more detail, see demo folder.
