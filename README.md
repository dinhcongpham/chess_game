# Pygame Chess Game

Dự án này là một trò chơi cờ vua hai người chơi được phát triển bằng thư viện Pygame trong Python. Trò chơi cung cấp giao diện đồ họa đơn giản và triển khai các quy tắc cờ vua cơ bản, cho phép hai người chơi đấu với nhau trên cùng một máy tính.

## Chức năng chính

Dự án đã triển khai thành công các chức năng cốt lõi của một ván cờ vua:

* **Phát hiện chiếu (Check Detection):** Hệ thống có khả năng nhận biết khi nào quân Vua của một bên đang bị chiếu bởi quân cờ của đối phương và hiển thị cảnh báo.
* **Nhập thành (Castling):** Hỗ trợ luật chơi nhập thành cho cả quân Vua Trắng và Đen, cho phép di chuyển Vua và Xe cùng lúc theo đúng quy định.
* **Tạo nước đi hợp lệ (Legal Move Generation):** Tính toán và hiển thị chính xác các ô vuông mà quân cờ được chọn có thể di chuyển đến, tuân thủ luật đi của từng loại quân cờ (Tốt, Mã, Tượng, Xe, Hậu, Vua) và tránh các nước đi vào ô có quân cờ cùng màu.
* **Hiển thị quân cờ bị bắt (Visualization of Captured Pieces):** Các quân cờ bị loại khỏi bàn cờ sẽ được hiển thị ở khu vực riêng bên cạnh bàn cờ, giúp người chơi dễ dàng theo dõi số lượng và loại quân cờ đã bị bắt.

## Cài đặt

Để chạy trò chơi này, bạn cần cài đặt Python và thư viện Pygame.

1.  **Cài đặt Python:**
    Nếu bạn chưa có Python, hãy tải và cài đặt phiên bản phù hợp với hệ điều hành của bạn từ trang web chính thức:
    [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **Cài đặt Pygame:**
    Mở Terminal hoặc Command Prompt và chạy lệnh sau để cài đặt thư viện Pygame:
    ```bash
    pip install pygame
    ```

3.  **Tải mã nguồn và tài nguyên:**
    Tải file `main.py` (chứa mã nguồn trò chơi) và đảm bảo bạn có thư mục `assets/images` chứa các file hình ảnh của các quân cờ (như `black bishop.png`, `white king.png`, v.v.). Đặt file `main.py` và thư mục `assets` cùng cấp trong một thư mục dự án. Cấu trúc thư mục sẽ trông như sau:

    ```
    your_project_folder/
    ├── main.py
    └── assets/
        └── images/
            ├── black bishop.png
            ├── black king.png
            ├── black knight.png
            ├── black pawn.png
            ├── black queen.png
            ├── black rook.png
            ├── white bishop.png
            ├── white king.png
            ├── white knight.png
            ├── white pawn.png
            ├── white queen.png
            └── white rook.png
    ```

## Cách chạy

Sau khi đã hoàn tất cài đặt và sắp xếp file, mở Terminal hoặc Command Prompt, điều hướng đến thư mục `your_project_folder` và chạy lệnh sau:

```bash
python main.py