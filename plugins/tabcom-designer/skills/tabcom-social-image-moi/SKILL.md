---
name: tabcom-social-image-moi
description: BẢN MỚI — quy trình Ý TƯỞNG TRƯỚC cho ảnh social Tabcom (dịch vụ vận hành gian hàng Shopee/TikTok Shop). Rút thông điệp, động não 8–10 ý tưởng hình (mỗi ý một lối nghĩ, gắn một thủ pháp bố cục, chấm điểm) để người dùng chọn, rồi tự thiết kế trong "giọng hình" Tabcom (ảnh thật/3D có nắng, texture, chữ chọn theo thông điệp, mascot túi cam khi cần chất Shopee), soát prompt, Codex render 1 lần, dán logo bằng code, soát bằng số và ghi gu người dùng. Không bám bố cục mẫu nào. Dùng khi người dùng nói "skill mới", "bản mới", "làm kiểu mới", "brainstorm ảnh", "động não ý tưởng ảnh", "nghĩ ý tưởng cho bài này", hoặc yêu cầu ảnh social Tabcom mà không gửi mẫu để bám. Quy trình bám mẫu nằm ở skill tabcom-social-image-cu.
---

# Tabcom social image — BẢN MỚI (ý tưởng trước)

Bản cũ (bám mẫu Pinterest, đổi 3 dấu vân tay): skill `tabcom-social-image-cu`.

Luồng dừng người dùng **đúng 1 lần**: sau khi đưa bảng động não (M2), chờ người dùng chọn 1–2 ý. Chọn xong thì chạy thẳng tới ảnh hoàn thiện.

## Tinh thần (người dùng dạy — không được quên)
1. **Ý tưởng trước, mẫu chỉ để học kỹ thuật.** Không đính kèm ảnh mẫu cho Codex, không chép bố cục của mẫu nào.
2. **Mọi lựa chọn phải suy ra từ thông điệp.** Kiểu chữ, vị trí chữ, nền, ánh sáng đều phải kể đúng thông điệp. Khi người dùng khen, họ khen cách nghĩ, không phải công thức: **không lặp lại** cặp font hay bố cục của bài vừa được khen.
3. **Giữ một giọng hình cho Tabcom.** Khi bị chê, hỏi xem sai ở đâu, không nhảy sang phong cách khác (flat, riso…). Nhảy phong cách làm thương hiệu bị loạn.
4. **Ảnh phải tượng hình**, nhìn 1 giây là hiểu. Ảnh phải thấy ngay sự liên quan tới Shopee/TMĐT.
5. **Mỗi lần render là một phiên bản riêng** (`v1`, `v2`… hoặc `y1`, `y7`…). Không ghi đè, không xoá bản cũ, vì người dùng cần so sánh.
6. **Mặc định khổ 1:1 (1080×1080).** Không tự đổi tỷ lệ.

## Nguồn đọc trước mỗi lần làm
- `${CLAUDE_PLUGIN_ROOT}/brand/gu-nguoi-dung.md` và `outputs/gu-nguoi-dung.md` (bản riêng của bạn, nếu có): nhật ký khen/chê kèm lý do. **Đọc hết cả hai** trước khi động não.
- `${CLAUDE_PLUGIN_ROOT}/brand/kho-thu-phap-bo-cuc.md` và `outputs/kho-thu-phap-bo-cuc.md` (nếu có): 13 thủ pháp bố cục T1–T13 và luật dùng.
- `${CLAUDE_PLUGIN_ROOT}/brand/TABCOM-BRAND-VISUAL-GUIDELINE.md`: mục 0 (quy tắc cứng), mục 4 (màu).
- `${CLAUDE_PLUGIN_ROOT}/docs/huong-dan-design-co-ban.md`: phân cấp, căn gióng, tương phản.

Đường dẫn: `SK` = thư mục skill này. Logo trắng: `${CLAUDE_PLUGIN_ROOT}/assets/logos/tabcom-white-green-transparent.png`.
Logo navy: `.../tabcom-navy-green-transparent.png`. Thư mục bàn giao: `outputs/hinh-anh/yy.mm.dd - <ten-bai-khong-dau>/`.

**Cần có trên máy:** [Codex CLI](https://github.com/openai/codex) đã đăng nhập (lệnh `codex`, dùng để tạo ảnh), Python 3.10+ với `pip install pillow numpy`. Thiếu gì thì báo người dùng cài trước. Thư mục `outputs/` tính từ thư mục đang làm việc, không ghi vào thư mục plugin.

## M1. Thông điệp
- Rút **1 câu thông điệp** và tiêu đề trên ảnh ≤ 8 từ. Viết như người Việt nói: câu ngắn, động từ mạnh, không danh từ hoá.
- Thông điệp thường có cấu trúc: căng → buông, trên ↔ dưới, chậm ↔ nhanh, trước → sau. Ghi rõ cấu trúc đó, vì đó là nguyên liệu để chọn chữ.
- Người dùng chưa cho chủ đề thì tự chọn một nỗi đau thật của chủ shop mới, nói rõ đã chọn gì.

## M2. Động não 8–10 ý (chỉ dùng chữ, không render)
Lưu `dong-nao.md` trong thư mục bài. Mỗi ý **một lối nghĩ khác nhau**, chọn trong các lối:
ẩn dụ · phóng đại · đối lập trước/sau · chơi chữ tiếng Việt · cảnh đời thường Việt (chợ, võng, trà đá…) ·
biến con số thành vật thể · UI kể chuyện · nhân vật ẩn dụ / mascot · góc nhìn bất ngờ · âm thanh thành hình.
- Mỗi ý gắn **1 thủ pháp** `T#` trong kho. **Không dùng lại thủ pháp chính của bài ngay trước.**
- Mỗi ý viết 2–3 dòng: hình gì, bố cục gì, chữ gì.
- Chấm 1–5 theo 4 tiêu chí: **Bất ngờ · Hiểu trong 1 giây · Chất Việt/Shopee · An toàn** (pháp lý, văn hoá).
- Đề xuất 2–3 ý kèm lý do. **Dừng, chờ người dùng chọn** (được chọn 2 ý để render cả hai).

## M3. Thiết kế chi tiết ý được chọn
**Giọng hình Tabcom** (đã được người dùng duyệt qua các bài võng, cõng thẻ giá, ốc sên):
- **Ảnh thật hoặc 3D polished**, nắng chiều ấm qua rèm lá sách, bóng mềm, có hạt film và texture in nhẹ. Không làm ảnh phẳng, không làm riso.
- **Thế giới chung:** tường vữa xanh `#1173C8 → #2194FC` có vân bay, sàn gạch men kem. Được đổi bối cảnh khi ý tưởng cần, nhưng giữ ánh sáng và chất liệu.
- **Khi cần chất Shopee:** dùng **mascot 3D túi mua sắm cam `#EE4D2D`** (quai như tai, mắt to, găng tay trắng), mỗi con một biểu cảm, **không in logo hay chữ S**. Giao diện chat/app dùng header cam, chỉ nằm trong màn hình thật.
- **Nhân vật phụ** mặc đồ đời thường nhiều màu (váy vàng, áo hoa…). Người dùng thích vì thực tế và tinh nghịch. Bộ màu thương hiệu chỉ áp cho nền, chữ, đồ hoạ.
- **Nhân vật chính:** người Việt, áo polo xanh `#1173C8`.

**Chữ suy ra từ thông điệp**, ví dụ:
- võng: "BẠN NGỦ," đứng nặng → "đơn vẫn về." nghiêng nhẹ;
- cõng thẻ giá: "Phí ngồi trên," đặt trên cao, "chủ shop gánh dưới." đặt sát sàn;
- ốc sên: "Rep kiểu ốc sên," giãn chữ chậm → "khách đi từ lâu." nghiêng, có vệt tốc độ.

Độ đậm vừa phải (SemiBold/Bold), **không dồn chữ siêu đậm hay mảng đen** ở nhiều chỗ (người dùng chê "nặng mắt").

**Chữ trắng luôn có bóng đổ mềm:** một lớp bóng tối nhẹ, loang rộng, lệch xuống dưới chữ để chữ không chìm vào nền (người dùng duyệt qua bản dây giày tạo bằng ChatGPT). Đây là bóng tối, không phải glow. Ghi vào prompt: "soft, wide, low-opacity dark drop shadow under the white text for legibility — not a glow, not a hard outline".

**Bố cục:** ghi nhịp dọc bằng % cho từng tầng (chữ, nhân vật, vật chính, chữ dưới). **Cân trên và dưới**, không để một dải trống lớn ở giữa, không dồn hết nội dung lên trên.

## M4. Viết prompt (`prompt-vN.md`, tự đủ, không đính kèm ảnh)
Khung prompt:
```
Generate ONE image with your image generation tool. Do not read any files, do not run any shell commands, do not write code. Just call image generation once with the brief below, then reply "done".
=== IMAGE BRIEF ===        khổ + thông điệp + ý tưởng hình (1–2 câu) + style
=== BACKGROUND + TEXTURE ===
=== SCENE / CHARACTERS ===  liệt kê đủ mọi vật kèm số lượng, vị trí % ; "Exactly these … Nothing else."
=== TYPOGRAPHY ===          từng dòng: vị trí %, màu, độ đậm, cap height px, VÌ SAO chọn kiểu đó
=== LAYOUT RULES ===        vùng TRỐNG cho logo/domain, nhịp dọc, cân trên–dưới, màu
=== DO NOT ===
```
- **Không cho Codex vẽ logo.** Codex luôn vẽ logo to gấp 1,5–2 lần. Chừa vùng tường trống (ví dụ `x 70–96%, y 2–8%`) rồi dán logo bằng code.
- Nhân vật Việt: tả gương mặt (Đông Á, mắt một mí hoặc hai mí nhẹ, sống mũi thấp nhỏ), da sáng tông ấm, tóc đen, kèm câu cấm "NOT South Asian, Indian, Middle Eastern or Western". Tả rõ giải phẫu: "exactly two arms, two legs, five fingers". Tư thế phức tạp như nằm võng dễ lỗi chân, nên tả cụ thể vị trí chân.

## M5. Soát prompt (bắt buộc, trước khi render — sau bước này chỉ render 1 lần)
- [ ] Cỡ chữ nhỏ nhất ghi **≥ 26 px** (Codex hay vẽ nhỏ hơn yêu cầu; chuẩn trên ảnh là ≥ 22 px).
- [ ] Chữ trắng chỉ đặt trên nền đậm. Trên sàn hoặc nền sáng thì dùng navy `#05173D`.
- [ ] Lề chữ ≥ 64 px. Các dòng căn giữa cùng tâm `x = 540`.
- [ ] Nhịp dọc cân trên–dưới. Chữ không chạm nhân vật.
- [ ] Độ đậm: không có ≥ 2 khối siêu đậm hoặc đen đặc cùng lúc.
- [ ] Rủi ro pháp lý/văn hoá: **không cắt, xé, đốt, làm hỏng tiền Việt Nam**; không chân dung lãnh tụ; không cờ; không logo Shopee/TikTok hay chữ S; không thương hiệu khác.
- [ ] Ghi đủ vùng trống cho logo và domain.
- [ ] Không có câu tự mâu thuẫn hay câu sót từ prompt cũ (đọc lại toàn bộ, tìm các chữ như "wait", số liệu trái nhau).
- [ ] Không lạc khỏi giọng hình Tabcom (M3).
- [ ] Mỗi dòng chữ ghi "natural proportions, never horizontally squeezed or stretched" và chừa đủ bề ngang cho số ký tự (ước ~0,55 × cap height mỗi ký tự với Inter). Hiệu ứng chữ có chủ đích ≠ chữ bị co kéo méo (người dùng chê ở bản quẹt trái v3).

## M6. Render — 1 lần
```
python -I "SK/scripts/codex_image.py" --prompt prompt-vN.md --out vN-codex.png --size 1080x1080
```
- **Không chạy 2 lệnh Codex song song.** Render nhiều ý thì chạy tuần tự trong một lệnh.
- **Codex hay treo sau khi đã tạo xong ảnh.** Nếu chạy quá khoảng 7 phút: xem `~/.codex/generated_images/<phiên mới nhất>/exec-*.png`. Có ảnh thì tự scale-cover rồi crop giữa về 1080×1080 và lưu `vN-codex.png`. Có thể đặt `timeout 420` cho lệnh.

## M7. Dán logo và domain bằng code
- Logo **trắng** trên nền đậm, **navy** trên nền sáng, rộng 160–200 px. Domain `tabcomgroup.vn` Segoe UI Bold **22 px**.
- Mặc định: logo ở góc trên và domain ở góc đối diện cùng tâm dọc, **hoặc** logo với domain căn phải ngay dưới logo.
- Đo màu nền vùng định đặt: tương phản với logo/domain phải ≥ 4,5:1. **Tránh vệt nắng sáng** (logo trắng sẽ chìm).
- Cách chữ hoặc vật ≥ 20 px.
- Không xoá logo do Codex tự vẽ khi logo đó đè lên người hay vật (inpaint sẽ làm nhòe, đã hỏng 1 lần).
- Lưu `vN-final.png`.

## M8. Soát bằng số (A7), ghi `doi-chieu-vN.md`
- `python -I "SK/scripts/qa_measure.py" vN-final.png`. Nếu báo `busy_background` thì đo tay: hộp bao từng khối chữ, lề, tâm trục, tương phản WCAG.
- Crop phóng to ×2 từng khối chữ để soát **dấu tiếng Việt**. Crop mặt để soát người Việt. Soát tay chân đủ và đúng khớp.
- Bảng: nguyên tắc · số đo · đạt hay không · do Codex hay do prompt. Lỗi do prompt thì thêm dòng soát mới vào M5.

## M9. Bàn giao
Mở ảnh (hoặc tờ so sánh khi có nhiều bản). Báo ngắn:
- ý tưởng và thủ pháp;
- chữ chọn vì sao;
- đã sửa gì bằng code;
- lỗi còn lại;
- token đã dùng.

Không liệt kê lại những thứ đã ổn qua nhiều lượt.

## M10. Sau phản hồi của người dùng
- Ghi ngay một dòng vào `outputs/gu-nguoi-dung.md` (tạo nếu chưa có; không sửa bản trong plugin vì bị ghi đè khi cập nhật) theo dạng: ngày · bài/bản · phản hồi · lý do rút ra.
- Gặp thủ pháp mới thì thêm vào `outputs/kho-thu-phap-bo-cuc.md`.
- Sửa theo góp ý thì làm phiên bản mới (`v(N+1)`) và vẫn soát M5. Góp ý tới giữa lúc đang render thì báo rõ bản vừa ra chưa có góp ý đó.
