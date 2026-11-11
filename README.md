# Tabcom Designer – plugin thiết kế ảnh social cho Claude Code

Plugin cài vào Claude Code một agent designer chuyên làm ảnh bài đăng social cho Tabcom (dịch vụ vận hành gian hàng Shopee/TikTok Shop). Claude viết prompt, Codex vẽ ảnh, rồi Claude tự soát ảnh bằng số đo.

Có 2 cách làm:

- **Bản cũ – bám mẫu** (`tabcom-social-image-cu`): tìm 3–5 mẫu banner nước ngoài trên Pinterest để bạn chọn. 8 agent phân tích mẫu song song (phân cấp, xếp lớp, căn gióng, xa gần, khoảng trống, chữ, màu, hình). Sau đó giữ bố cục, đổi 3 "dấu vân tay" để không thành bản sao, áp màu và logo Tabcom.
- **Bản mới – ý tưởng trước** (`tabcom-social-image-moi`): rút thông điệp, đưa 8–10 ý tưởng hình có chấm điểm để bạn chọn, rồi thiết kế theo "giọng hình" Tabcom: ảnh thật có nắng, mascot túi cam, chữ chọn theo thông điệp.

Cả hai chỉ dừng hỏi bạn một lần, mỗi ảnh chỉ render một lần, mọi khâu soát làm trên prompt trước khi render.

Chia sẻ bởi **Nhật Dương** · [Facebook](https://www.facebook.com/nhatduong.vn) · [YouTube](https://www.youtube.com/@Under30vn) · [TikTok](https://www.tiktok.com/@nhatduong.vn)

## Cài đặt

Chạy một lệnh trong terminal. Lệnh này cài plugin và **bật tự động cập nhật**.

**Windows (PowerShell):**

```powershell
curl.exe -fsSL https://raw.githubusercontent.com/Annie-246/tabcom-designer-plugin/main/install.js | node -
```

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/Annie-246/tabcom-designer-plugin/main/install.js | node -
```

Khởi động lại Claude Code sau khi cài.

### Cài trong Claude Code

```
/plugin marketplace add https://github.com/Annie-246/tabcom-designer-plugin.git
/plugin install tabcom-designer@tabcom-plugins
```

Cách này chưa bật tự động cập nhật. Muốn bật: gõ `/plugin`, vào tab **Marketplaces**, chọn `tabcom-plugins`, chọn **Enable auto-update**.

## Dùng

Mở Claude Code trong thư mục làm việc và nói:

> Giúp tôi tạo hình ảnh dạng A cho bài viết có tiêu đề "5 lỗi khiến shop TikTok mới không ra đơn"

Muốn làm kiểu ý tưởng trước thì nói thêm "dùng skill mới" hoặc "brainstorm ảnh cho bài này". Gửi kèm một ảnh và nói "biến ảnh này thành của Tabcom" thì agent bỏ bước tìm Pinterest và dùng luôn ảnh đó.

Kết quả nằm ở `outputs/hinh-anh/yy.mm.dd - <ten-bai>/` trong thư mục làm việc: ảnh cuối, ảnh Codex gốc, prompt, bản phân tích và bảng đối chiếu. Phản hồi khen/chê của bạn được ghi vào `outputs/gu-nguoi-dung.md` để lần sau Claude làm hợp gu hơn.

Dạng B (case study) chưa có quy trình.

## Trong plugin có gì

| Thư mục | Nội dung |
|---|---|
| `agents/` | `tabcom-designer` (agent chính) và `tabcom-ref-analyst` (phân tích một khía cạnh của ảnh mẫu) |
| `skills/` | 2 quy trình bám mẫu và ý tưởng trước, kèm script gọi Codex, đo lề, tìm Pinterest |
| `brand/` | Guideline nhận diện Tabcom, mã màu, thành phần cắt sẵn, kho thủ pháp bố cục, nhật ký gu, script vẽ phác thảo |
| `assets/` | Logo Tabcom trắng và navy, font Be Vietnam Pro cho phác thảo |
| `docs/` | Hướng dẫn design cơ bản: phân cấp, căn gióng, xa gần, chữ, màu, checklist |

## Cần có

- [Claude Code](https://claude.com/claude-code)
- [Codex CLI](https://github.com/openai/codex) đã đăng nhập (lệnh `codex`), dùng để tạo ảnh
- Python 3.10+ và `pip install pillow numpy`
- Cho bản bám mẫu: Pinterest MCP (`npm i -g pinterest-mcp-server`, rồi thêm vào Claude Code bằng `claude mcp add pinterest -s user -- pinterest-mcp-server`)

## Giấy phép

Code và tài liệu theo giấy phép MIT. Logo, tên và bộ nhận diện Tabcom thuộc về Tabcom, chỉ dùng để làm ảnh cho Tabcom. Font Be Vietnam Pro theo giấy phép SIL OFL (`assets/fonts/be-vietnam-pro/OFL.txt`).
