
# output_handler module<br>
Manages output of extracted data or errors.<br>
1.Prints extracted IOC dictionaries or error messages to the console if no output file is specified.<br>
2.Appends the JSON-formatted data or errors to an output file if a filename is provided.<br>
3.Keeps output logic separate from parsing and extraction logic.<br>

---
### Comments<br>
\#a.1 calls print_output() or write_output() based on the user preference like if the user wants the output in the screen or to a file<br><br>
\#c.1 if the user doesn't provides value for format then by default the value of format is equal to ndjson<br>
\#c.2 the results will be shown in the terminal<br>
\#c.3 dictobject.items() gives us a viewobject of the dictionary, when we iterate over it we get 2-element tuples (key,value) pairs.<br><br>
\#.d.1 In storage or transmission (like in a file or over a network), all JSON data is ultimately text, i.e., a string of characters.
But conceptually and semantically, we distinguish types inside the JSON: json objects, array, string, number. Everything is text when written to a file, but JSON parsers know how to interpret that text and restore the correct type in memory.<br>
\#d.2 Python automatically concatenates adjacent string literals inside parentheses, and this works for multi-line strings too. This is called implicit string concatenation. Note, that there are no commas between those strings.<br><br>
