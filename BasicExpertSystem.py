while True:
    try:
        choice = input("\nBạn muốn làm gì? (học / xem phim / tạm biệt): ").lower()
        if "học" in choice:
            print(" Chúc bạn học tập tốt, nhớ giữ gìn sức khoẻ bạn nhé!")
        elif "xem phim" in choice:
            print("Bạn muốn xem thể loại nào?")
            TheLoai = input(" Nhập thể loại (Hành động, Tình cảm, Trinh thám, Kinh dị, Hoạt hình): ").lower()
            movies = {
                "hành động": ["Thần điêu đại hiệp", "Lãng Khách", "Kẻ săn người - Mouse"],
                "tình cảm": ["Khó dỗ dành", "Mắt biếc", "Ngoại tình"],
                "trinh thám": ["Sherlock Holmes", "Sự im lặng của bầy cừu", "Thám tử mù"],
                "kinh dị": ["Vong nhi", "Kẻ ăn hồn", "Ma búp bê"],
                "hoạt hình": ["Thám tử lừng danh Conan", "Sakura thủ lĩnh thẻ bài", "Công chúa Ori"]
            }
            if TheLoai in movies:
                print(" Gợi ý phim cho bạn:")
                for i, movie in enumerate(movies[TheLoai], start=1):
                    print(f"{i}. {movie}")
                print("Chúc bạn xem phim vui vẻ!")
            else:
                print(" Xin lỗi, tôi chưa có gợi ý cho thể loại này.")

        elif "tạm biệt" in choice:
            print("Tạm biệt, hẹn gặp lại!")
            break

        else:
            print(" Tôi chưa hiểu, hãy chọn 'học', 'xem phim' hoặc 'tạm biệt'.")

    except:
        print("Lỗi, hãy nhập lại.")
