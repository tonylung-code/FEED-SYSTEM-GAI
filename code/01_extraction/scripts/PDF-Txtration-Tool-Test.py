import opendataloader_pdf


input_path = "C:\\Users\\e11338\\Desktop\\Feed System GAI\\data\\上銀滾珠螺桿.pdf"
# # Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path = input_path,
    output_dir="C:\\Users\\e11338\\Desktop\\Feed System GAI\\data",
    format="json,html,pdf,markdown",
)