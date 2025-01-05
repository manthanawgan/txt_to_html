def gamess_to_html(gamess_text):
    """
    Converts GAMESS input text into HTML formatted code.
    """
    html_output = ["<html>", "<head><title>GAMESS Input Filed</title></head>", "<body>", "<pre>"]
    
    lines = gamess_text.strip().split("\n")
    for line in lines:
        if line.startswith("$"):     # Highlight different sections with HTML
            section_name = line.split()[0].strip()
            html_output.append(f"<strong>{line}</strong>")
        elif line.strip().startswith("!"):
            html_output.append(f"<em>{line}</em>")   # Comments are italicized
        else:
            html_output.append(line)

    html_output.extend(["</pre>", "</body>", "</html>"])
    return "\n".join(html_output)


# Example GAMESS input file as a string
gamess_input = """
$CONTRL SCFTYP=UHF MAXIT=200 RUNTYP=OPTIMIZE
         COORD=UNIQUE MULT=1 
         ICHARG=5  
         DFTTYP=B3LYP
         MOLPLT=.FALSE. PLTORB=.FALSE.  $END
 $SYSTEM TIMLIM=2879 MWORDS=250  $END

 $FORCE METHOD=SEMINUM NVIB=2 $END 
 $STATPT OPTTOL=0.0005 NSTEP=999 $END
 $STATPT IHREP=0 HSSEND=.TRUE.  $END

 $DFT    METHOD=GRID  NLEB=590  $END

 $BASIS  GBASIS=N31 NGAUSS=6
         NDFUNC=1   NPFUNC=0  $END

 $PCM  SOLVNT=H2O  $END

 $SCF    DIRSCF=.T. $END
 $GUESS  GUESS=HUCKEL  $END

 $DATA
 
 $END
"""

# Convert to HTML
html_code = gamess_to_html(gamess_input)

# Save the HTML to a file
with open("gamess_input.html", "w") as file:
    file.write(html_code)

print("HTML file created successfully!")
