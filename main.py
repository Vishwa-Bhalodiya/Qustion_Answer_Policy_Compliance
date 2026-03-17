from fastapi import FastAPI, UploadFile, File
import uvicorn

from compare_service import compare_documents
from text_utils import extract_text

app = FastAPI()


@app.post("/compare-policies/")
async def compare_policies(
    client_file: UploadFile = File(...),
    vendor_file: UploadFile = File(...)
):
    try:
        # Step 1: Extract full text
        client_text = extract_text(client_file)
        vendor_text = extract_text(vendor_file)

        # Step 2: Single Mistral call
        result = compare_documents(client_text, vendor_text)

        return result

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)