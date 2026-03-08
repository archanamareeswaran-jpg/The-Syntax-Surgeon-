import gradio as gr

def fix_syntax(code):
    try:
        compile(code, "<string>", "exec")
        return "No Syntax Errors Found!"
    except SyntaxError as e:
        return f"Syntax Error:\n{e}"

interface = gr.Interface(
    fn=fix_syntax,
    inputs=gr.Code(language="python"),
    outputs="text",
    title="Syntax Surgeon"
)

interface.launch()
