import os
import re

files_to_process = [
    r"c:\laragon\www\portoku\data-science-data-analysis\clustering-kondisi-ekonomi-provinsi.html",
    r"c:\laragon\www\portoku\data-science-data-analysis\sentiment-analysis-tokopedia-reviews.html",
    r"c:\laragon\www\portoku\front-end\buyheart-ecommerce.html",
    r"c:\laragon\www\portoku\front-end\company-profile.html",
    r"c:\laragon\www\portoku\front-end\sim-apotik-pos.html",
    r"c:\laragon\www\portoku\front-end\yayasan-haadii-nurul-ikhlas.html",
    r"c:\laragon\www\portoku\ui-ux\brewmo-coffee-app.html"
]

neo_config = """    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              "neo-bg": "#f4f4f0",
              "neo-yellow": "#ffe600",
              "neo-pink": "#ff90e8",
              "neo-cyan": "#23f0ff",
              "neo-green": "#00e59b",
              "neo-orange": "#ff6b00",
              "neo-purple": "#b28dff",
            },
            fontFamily: {
              sans: ["Plus Jakarta Sans", "sans-serif"],
            },
            boxShadow: {
              'neo': '8px 8px 0px 0px rgba(0,0,0,1)',
              'neo-sm': '4px 4px 0px 0px rgba(0,0,0,1)',
              'neo-hover': '2px 2px 0px 0px rgba(0,0,0,1)',
            },
          },
        },
      };
    </script>
    <style type="text/tailwindcss">
      @layer base {
        body {
          @apply bg-neo-bg text-black font-sans antialiased selection:bg-neo-cyan selection:text-black;
        }
      }
      @layer components {
        .detail-card {
          @apply bg-white border-4 border-black rounded-2xl p-8 md:p-10 transition-all duration-200 shadow-neo;
        }
        .dock-item {
          @apply flex flex-col items-center justify-center p-2 rounded-xl transition-all duration-200 min-w-[64px] text-black font-bold border-2 border-transparent hover:border-black hover:bg-neo-pink hover:shadow-neo-sm;
        }
        .dock-item.active {
          @apply bg-neo-yellow border-black shadow-neo-sm;
        }
        .tech-badge {
          @apply px-4 py-2 bg-white border-2 border-black rounded-xl text-sm font-extrabold text-black hover:bg-neo-yellow transition-all shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] cursor-default;
        }
        .table-header {
          @apply px-6 py-4 text-left text-xs font-extrabold uppercase tracking-wider text-black border-b-4 border-black bg-neo-pink;
        }
        .table-cell {
          @apply px-6 py-4 text-sm font-bold text-black border-b-2 border-black bg-white;
        }
      }
    </style>"""

for filepath in files_to_process:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace tailwind config and styles
    content = re.sub(r'<script>\s*tailwind\.config = \{.*?</style>', neo_config, content, flags=re.DOTALL)
    
    # Body tag
    content = re.sub(r'<body class="pb-32">', r'<body class="pb-32 bg-[url(\'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9IiMwMDAiIGZpbGwtb3BhY2l0eT0iMC4wNSIvPjwvc3ZnPg==\')]">', content)
    
    # Generic text color fixes
    content = content.replace('text-white', 'text-black')
    content = content.replace('text-gray-400', 'text-black')
    content = content.replace('text-gray-500', 'text-black')
    
    # Replace standard banners
    content = content.replace('rounded-[2.5rem] overflow-hidden border border-border-subtle shadow-[0_40px_100px_rgba(0,0,0,0.5)]', 
                              'rounded-3xl overflow-hidden border-8 border-black shadow-[12px_12px_0px_0px_rgba(0,0,0,1)]')
    
    # Fix category tag
    content = re.sub(r'inline-block px-4 py-1\.5 border border-acid-lime text-acid-lime text-xs font-bold uppercase tracking-\[0\.2em\] rounded-full mb-8 bg-acid-lime/5',
                     r'inline-block px-4 py-1.5 border-4 border-black bg-neo-yellow text-black text-xs font-extrabold uppercase tracking-[0.2em] rounded-full mb-8 shadow-neo-sm transform -rotate-1', content)

    # Make main H1 bold with stroke
    content = re.sub(r'(<h1[^>]*class="[^"]*?)font-bold([^"]*?")', r'\1font-extrabold\2 style="-webkit-text-stroke: 1px black;"', content)
    
    # Fix paragraph hero
    content = re.sub(r'<p\s+class="text-xl text-black font-normal leading-relaxed max-w-2xl mx-auto mb-10">',
                     r'<p class="text-xl text-black font-bold leading-relaxed max-w-3xl mx-auto mb-10 bg-white border-4 border-black p-4 rounded-xl shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transform rotate-1">', content)
    
    content = re.sub(r'<p\s+class="text-xl text-black font-normal leading-relaxed max-w-3xl mx-auto mb-10">',
                     r'<p class="text-xl text-black font-bold leading-relaxed max-w-3xl mx-auto mb-10 bg-white border-4 border-black p-4 rounded-xl shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transform rotate-1">', content)

    # Date / Role boxes
    content = content.replace('border-y border-border-subtle', 'border-y-4 border-black bg-white shadow-neo-sm')
    content = content.replace('<i class="far fa-calendar-alt text-acid-lime"></i>', '<div class="bg-neo-pink border-2 border-black p-2 rounded-lg shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]"><i class="far fa-calendar-alt"></i></div>')
    content = content.replace('<i class="fas fa-user text-acid-lime"></i>', '<div class="bg-neo-cyan border-2 border-black p-2 rounded-lg shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]"><i class="fas fa-user"></i></div>')

    # View Source Code / Github button
    content = re.sub(r'px-8 py-4 bg-white text-black font-bold rounded-full hover:bg-acid-lime transition-all flex items-center gap-2 group',
                     r'px-8 py-4 bg-neo-purple text-black border-4 border-black font-extrabold text-xl uppercase rounded-xl shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:bg-neo-green hover:translate-y-1 hover:translate-x-1 hover:shadow-[3px_3px_0px_0px_rgba(0,0,0,1)] transition-all flex items-center gap-3 group', content)
    
    content = re.sub(r'px-8 py-4 bg-white/5 border border-border-subtle font-bold rounded-full hover:bg-white/10 transition-all flex items-center gap-2',
                     r'px-8 py-4 bg-neo-yellow text-black border-4 border-black font-extrabold text-xl uppercase rounded-xl shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:bg-neo-pink hover:translate-y-1 hover:translate-x-1 hover:shadow-[3px_3px_0px_0px_rgba(0,0,0,1)] transition-all flex items-center gap-3', content)

    # h3 inside detail cards
    content = re.sub(r'<h3 class="text-2xl font-bold mb-6 flex items-center gap-3">\s*<span class="w-8 h-1 bg-acid-lime rounded-full"></span>',
                     r'<h3 class="text-3xl font-extrabold mb-6 flex items-center gap-3 uppercase">\n              <span class="w-8 h-8 border-4 border-black bg-neo-yellow rounded-full shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]"></span>', content)

    # Project Status
    content = content.replace('bg-acid-lime items-center text-center group cursor-pointer border-none', 'bg-neo-green')
    content = content.replace('<i class="fas fa-rocket text-4xl text-black mb-4 group-hover:-translate-y-2 transition-transform"></i>', '<div class="bg-white border-4 border-black rounded-full w-16 h-16 flex items-center justify-center mb-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] mx-auto"><i class="fas fa-rocket text-3xl"></i></div>')
    
    # Project Status specific for some files
    content = content.replace('bg-acid-lime text-black border-none', 'bg-neo-green')
    content = content.replace('<i class="fas fa-chart-pie text-4xl mb-4"></i>', '<div class="bg-white border-4 border-black rounded-full w-16 h-16 flex items-center justify-center mb-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] mx-auto"><i class="fas fa-chart-pie text-3xl"></i></div>')

    # Nav
    content = content.replace('bg-dark-surface/80 backdrop-blur-2xl border border-white/10 p-2 rounded-2xl flex gap-2 z-50 shadow-2xl', 'bg-white border-4 border-black p-2 rounded-2xl flex gap-2 z-50 shadow-neo')
    content = content.replace('dock-item active', 'dock-item active bg-neo-yellow border-black shadow-neo-sm')
    
    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Replacement script completed.")
