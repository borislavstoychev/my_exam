function updateImage() {
            const img = document.getElementById('img_preview');
            const url = this.value;
            img.src = url;
        }

        document.getElementById('img_input')
            .addEventListener('input', updateImage);