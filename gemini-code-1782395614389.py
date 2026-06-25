# Let's generate a highly polished, interactive application format. Since the user wants a "web or app" that they can immediately put on GitHub, 
# I will generate the complete standalone single-file source code (`index.html`) optimized for mobile devices (since it's for a crush, they will likely open it on phone).
# I'll embed a complete styled experience, incorporating Wafiy's name and phone number.

html_content = """<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Awak! ❤️</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: linear-gradient(135deg, #ffe5ec, #ffc2d1);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow-x: hidden;
            padding: 20px;
        }
        .card {
            background: rgba(255, 255, 255, 0.95);
            padding: 35px 25px;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(255, 71, 126, 0.2);
            text-align: center;
            max-width: 400px;
            width: 100%;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(255, 255, 255, 0.5);
        }
        .icon {
            font-size: 50px;
            margin-bottom: 15px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        h1 {
            color: #ff477e;
            font-size: 26px;
            margin-bottom: 15px;
            font-weight: 700;
        }
        p {
            color: #495057;
            font-size: 15px;
            line-height: 1.6;
            margin-bottom: 25px;
        }
        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            margin-top: 20px;
            position: relative;
            min-height: 60px;
        }
        button {
            padding: 14px 30px;
            border: none;
            border-radius: 50px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-weight: 600;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }
        .btn-yes {
            background: linear-gradient(45deg, #ff477e, #ff7096);
            color: white;
        }
        .btn-yes:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(255, 71, 126, 0.4);
        }
        .btn-no {
            background-color: #6c757d;
            color: white;
            transition: all 0.1s ease;
            z-index: 10;
        }
        
        /* Food Selection Grid */
        .food-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin: 20px 0;
        }
        .food-item {
            background: #fff;
            padding: 15px;
            border: 2px solid #f0f0f0;
            border-radius: 16px;
            cursor: pointer;
            font-size: 15px;
            font-weight: 500;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
        }
        .food-item:hover {
            border-color: #ffb3c6;
            background-color: #fff0f3;
        }
        .food-item.selected {
            border-color: #ff477e;
            background-color: #ffe5ec;
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(255, 71, 126, 0.15);
        }
        .food-emoji {
            font-size: 24px;
        }
        
        /* Date Picker Styling */
        input[type="date"] {
            padding: 14px;
            border-radius: 14px;
            border: 2px solid #ffccd5;
            font-size: 16px;
            width: 100%;
            margin-top: 10px;
            outline: none;
            color: #495057;
            background-color: #fff;
            font-family: inherit;
            text-align: center;
        }
        input[type="date"]:focus {
            border-color: #ff477e;
            box-shadow: 0 0 0 3px rgba(255, 71, 126, 0.2);
        }
        .hidden {
            display: none !important;
        }
    </style>
</head>
<body>

    <!-- LANGKAH 1: AJAK DATE -->
    <div id="step1" class="card">
        <div class="icon">✨</div>
        <h1>Hi Awak... 😊</h1>
        <p>Saya nak tanya sesuatu perkara penting ni... Sudi tak kalau awak keluar date dengan saya dalam masa terdekat?</p>
        <div class="btn-container" id="container1">
            <button class="btn-yes" onclick="nextStep(2)">Mesti lah Mau! ❤️</button>
            <button class="btn-no" id="noBtn" onmouseover="lariSikit()" onclick="lariSikit()">Tak Nak 😜</button>
        </div>
    </div>

    <!-- LANGKAH 2: PILIH TARIKH -->
    <div id="step2" class="card hidden">
        <div class="icon">🗓️</div>
        <h1>Yay! Hehe 🥰</h1>
        <p>Pilih tarikh bila yang awak rasa free:</p>
        <input type="date" id="datePicker">
        <div class="btn-container">
            <button class="btn-yes" style="width: 100%;" onclick="nextStep(3)">Seterusnya ➡️</button>
        </div>
    </div>

    <!-- LANGKAH 3: PILIH MAKANAN -->
    <div id="step3" class="card hidden">
        <div class="icon">🍕</div>
        <h1>Nak Makan Apa?</h1>
        <p>Pilih menu idaman awak (boleh pilih lebih daripada satu tahu):</p>
        <div class="food-grid">
            <div class="food-item" onclick="toggleFood(this, 'Pizza')">
                <span class="food-emoji">🍕</span><span>Pizza</span>
            </div>
            <div class="food-item" onclick="toggleFood(this, 'Pasta')">
                <span class="food-emoji">🍝</span><span>Pasta</span>
            </div>
            <div class="food-item" onclick="toggleFood(this, 'Coffee')">
                <span class="food-emoji">☕</span><span>Coffee</span>
            </div>
            <div class="food-item" onclick="toggleFood(this, 'Pastry')">
                <span class="food-emoji">🥐</span><span>Pastry</span>
            </div>
            <div class="food-item" onclick="toggleFood(this, 'Iskrim')">
                <span class="food-emoji">🍦</span><span>Ice Cream</span>
            </div>
            <div class="food-item" onclick="toggleFood(this, 'Sushi')">
                <span class="food-emoji">🍣</span><span>Sushi</span>
            </div>
        </div>
        <div class="btn-container">
            <button class="btn-yes" style="width: 100%;" onclick="hantarJawapan()">Selesai! ✨</button>
        </div>
    </div>

    <!-- LANGKAH FINAL: THANK YOU -->
    <div id="step4" class="card hidden">
        <div class="icon">💝</div>
        <h1>It's a Date! 🗓️❤️</h1>
        <p>Terima kasih! Maklumat dah dihantar ke WhatsApp Wafiy. Sila tunggu mesej balasan daripada Wafiy ya! 🥰</p>
    </div>

    <script>
        let dataDate = "";
        let selectedFoods = [];

        // Set min date to today so they cannot pick past dates
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('datePicker').setAttribute('min', today);

        function nextStep(step) {
            if (step === 3) {
                dataDate = document.getElementById('datePicker').value;
                if (!dataDate) {
                    alert("Pilihlah tarikh dulu kesayangan... 🥺");
                    return;
                }
            }
            document.getElementById('step1').classList.add('hidden');
            document.getElementById('step2').classList.add('hidden');
            document.getElementById('step3').classList.add('hidden');
            document.getElementById('step' + step).classList.remove('hidden');
        }

        function toggleFood(element, foodName) {
            element.classList.toggle('selected');
            if (selectedFoods.includes(foodName)) {
                selectedFoods = selectedFoods.filter(item => item !== foodName);
            } else {
                selectedFoods.push(foodName);
            }
        }

        // Trik butang "No" akan lari bila crush cuba nak tekan
        function lariSikit() {
            const noBtn = document.getElementById('noBtn');
            // Generate random movement within safe screen boundaries
            const x = Math.random() * (window.innerWidth - noBtn.offsetWidth - 40) - (window.innerWidth/2 - noBtn.offsetWidth);
            const y = Math.random() * (window.innerHeight - noBtn.offsetHeight - 40) - (window.innerHeight/2 - noBtn.offsetHeight);
            
            noBtn.style.position = 'absolute';
            noBtn.style.left = Math.max(10, Math.min(x, window.innerWidth - 100)) + 'px';
            noBtn.style.top = Math.max(10, Math.min(y, window.innerHeight - 100)) + 'px';
        }

        function hantarJawapan() {
            if (selectedFoods.length === 0) {
                alert("Pilihlah makanan kesukaan awak sekurang-kurangnya satu jom! 🥺");
                return;
            }
            
            // Format tarikh ke format tempatan
            const tarikhMesej = new Date(dataDate).toLocaleDateString('ms-MY', { 
                weekday: 'long', 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            });
            
            // Text template yang dihantar ke WhatsApp Wafiy
            const teksWhatsApp = `Hai Wafiy! Saya setuju nak keluar date dengan awak pada hari *${tarikhMesej}*. Nanti kita pergi makan *${selectedFoods.join(', ')}* sama-sama okay! 🥰`;
            
            // Menggunakan nombor telefon Wafiy: 601111892341
            const noTelefon = "601111892341"; 
            
            const urlWhatsApp = `https://wa.me/${noTelefon}?text=${encodeURIComponent(teksWhatsApp)}`;
            
            nextStep(4);
            
            // Buka WhatsApp automatik selepas 1.5 saat
            setTimeout(() => {
                window.open(urlWhatsApp, '_blank');
            }, 1500);
        }
    </script>
</body>
</html>
"""

# Save the code to a file so the user can easily download or access it.
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("File index.html generated successfully with Wafiy's details.")