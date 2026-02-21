import re

images = [
    "adarsh-singh.webp", "aman-kumar.webp", "anjali-yadav.webp", "ashfee-khan.webp", "astha-singh.webp",
    "avneesh-kumar-singh.webp", "ayush-kumar-pandey.webp", "chandan-kumar.webp", "deepak-pratap.webp", "deepika.webp",
    "gaurav.webp", "ishika-agarwal.webp", "komal-maurya.webp", "mohammad-navaid.webp", "monika-baghel.webp",
    "puja-kumari.webp", "sanjeev-kumar-singh.webp", "shobhika-rajput.webp", "sippal-rani.webp", "tausifraja.webp",
    "vaishali-vineet.webp", "yasha.webp"
]

template = """                    <!-- Student Card -->
                    <div class="w-[300px] shrink-0 group">
                        <div
                            class="bg-white rounded-2xl overflow-hidden shadow-[0_8px_30px_rgb(0,0,0,0.06)] border border-slate-100 hover:shadow-[0_20px_50px_rgba(0,87,163,0.15)] transition-all duration-500 hover:-translate-y-2">
                            <div class="relative h-52 overflow-hidden">
                                <img src="./images/placement/{img}"
                                    alt="Rahul Sharma"
                                    class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                                <div
                                    class="absolute inset-0 bg-gradient-to-t from-[#003c73]/80 via-transparent to-transparent">
                                </div>
                                <div class="absolute bottom-3 left-4 right-4">
                                    <span
                                        class="inline-block px-3 py-1 bg-[#ffc107] text-[#003c73] text-[10px] font-black uppercase tracking-wider rounded-full">Wipro</span>
                                </div>
                            </div>
                            <div class="p-5">
                                <h4 class="font-bold text-[#003c73] text-lg leading-tight">Rahul Sharma</h4>
                                <p class="text-[#50627b] text-sm mt-1">B.Tech CSE — Batch 2024</p>
                                <div class="flex items-center gap-2 mt-3">
                                    <div class="px-3 py-1 bg-blue-50 rounded-full text-[#0057a3] text-xs font-bold">₹6.5
                                        LPA</div>
                                    <div class="px-3 py-1 bg-[#fff8e1] rounded-full text-[#8a6a02] text-xs font-bold">
                                        Software Eng.</div>
                                </div>
                            </div>
                        </div>
                    </div>"""

cards = []
for i, img in enumerate(images):
    cards.append(template.format(index=i+1, img=img))

with open("/home/oxygen/Desktop/Accurate-Landing-v2/cards.html", "w") as f:
    f.write("\n".join(cards))
