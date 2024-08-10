# RGB lights control server
The remote RGB lights control server

## environment values
- **JWT_SECRET**
- **JWT_SECRET_OLD** (Optional, use it if you need to change secrets smoothly)
- **JWT_ALGORITHM** (By default "EdDSA")

## only 1 worker!
please use only one worker because the application stores the environment in global variables


**Description:** This server allows multiple clients to connect and synchronize RGB light settings.

## API Endpoints

### Get Color

- **Endpoint:** `/get-color`
- **Method:** `GET`
- **Summary:** Retrieve the current RGB color setting.
- **Operation ID:** `get_color_get_color_get`
- **Responses:**
  - **200 (Successful Response)**

### Set Color

- **Endpoint:** `/set-color`
- **Method:** `POST`
- **Summary:** Set a new RGB color.
- **Operation ID:** `set_color_set_color_post`
- **Request Body:**
  - **Content-Type:** `application/json`
  - **Schema:** RGB
  - **Required:** `true`
- **Responses:**
  - **200 (Successful Response)**
  - **423 (Locked)**
  - **422 (Validation Error)**
- **Security:** Requires JWT Bearer token.

### Synchronize Color Receiving

- **Endpoint:** `/synchronize-color-receiving`
- **Method:** `GET`
- **Summary:** Synchronize the receipt of color changes.
- **Operation ID:** `synchronize_color_receiving_synchronize_color_receiving_get`
- **Responses:**
  - **200 (Successful Response)**
