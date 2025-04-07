from django import forms
from django.utils.safestring import mark_safe

class RichTextEditorWidget(forms.Textarea):
    class Media:
        css = {
            "all": ["https://cdn.jsdelivr.net/npm/quill@1.3.6/dist/quill.snow.css"],
        }
        js = ["https://cdn.jsdelivr.net/npm/quill@1.3.6/dist/quill.min.js"]

    def render(self, name, value, attrs=None, renderer=None):
        if not value:
            value = ""  

        html = f"""
        <div id="editor-container" style="height: 200px;">{value}</div>
        <textarea name="{name}" id="hidden-textarea" style="display:none;">{value}</textarea>

        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                var quill = new Quill("#editor-container", {{
                    theme: "snow"
                }});

                quill.on("text-change", function() {{
                    document.getElementById("hidden-textarea").value = quill.root.innerHTML;
                }});
            }});
        </script>
        """
        return mark_safe(html) 
