tinymce.init({
  selector: "textarea", // Apply TinyMCE to all textareas
  height: 1000, // Set the height of the editor
  menubar: true, // Show the menubar at the top
  plugins: [
    "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen",
    "insertdatetime media table contextmenu directionality emoticons paste textcolor wordcount spellchecker",
    "code image",
  ],
  toolbar: [
    "undo redo | bold italic underline strikethrough | fontselect fontsizeselect | forecolor backcolor | alignleft aligncenter alignright alignjustify | outdent indent | numlist bullist | link image media | insertdatetime table | code fullscreen preview | emoticons | charmap",
    "cut copy paste | searchreplace | visualblocks code | wordcount spellchecker",
  ],
  menubar: "file edit insert view format table tools", // Menubar options
  file_picker_types: "image media", // Allow file picking for images and media files
  image_advtab: true, // Advanced image properties tab (resize, alignment, etc.)
  paste_as_text: true, // Paste as plain text (strips unnecessary formatting)
  content_css: "//www.tiny.cloud/css/codepen.min.css", // Optional content CSS (you can change this)
  branding: false, // Disable TinyMCE branding
  statusbar: true, // Show status bar with character count, etc.
  setup: function (editor) {
    // Example: Custom button addition (if needed)
    editor.ui.registry.addButton("mybutton", {
      text: "My Button",
      onAction: function () {
        alert("Button clicked!");
      },
    });
  },
});
