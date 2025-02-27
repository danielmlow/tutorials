VSCode: 

Add this to keybindings.json:
```    
    {
        "key": "cmd+enter",
        "command": "runCommands",
        "args": {
          "commands": [
            "jupyter.execSelectionInteractive",
            "cursorDown"
          ]
        },
        "when": "editorTextFocus && editorLangId == 'python'"
    },
```

This should run the line or highlighted text from a .py in a jupyter notebook and place the cursor in the next line. 

`jupyter.execSelectionInteractive` is the command ID for `Jupyter: run selection/line in Interactive Window`



## In interactive mode (runs higlighted text or line in Python/R console)
- Jupyter: run selection/line in Interactive Window: `cmd + enter`
- toggle comment: `cmd + /`
- end of line: `cmd + →`
- start of line: `cmd + ←`
- next word: `option + →`
- previous word: `option + ←`

## Jupyter notebook on VScode or colab 
- Execute Cell: `shift+cmd+enter` 
- Execute Cell and Select Below: `cmd+enter`
