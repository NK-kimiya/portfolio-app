const progressRing = document.querySelector('.progress-ring__circle');
const elment = document.getElementById('percentage-display-sentence').textContent;
        const progressText = document.querySelector('.progress-text');
        const circumference = 2 * Math.PI * 70; // 円の周の長さ（2πr）
        let currentProgress = 0; // 現在のプログレス
        const interval = 50; // アニメーション更新間隔(ms)
        const step = 1; // 一度に進むプログレスの量(%)
        const targetProgress = Number(elment); // アニメーションを停止させたいパーセンテージ

        function setProgress(percent) {
            const offset = circumference - percent / 100 * circumference;
            progressRing.style.strokeDasharray = `${circumference} ${circumference}`;
            progressRing.style.strokeDashoffset = offset;
            progressText.textContent = `${percent}%`; // テキストを更新
        }

        const animation = setInterval(() => {
            setProgress(currentProgress);
            if (currentProgress >= targetProgress) {
                clearInterval(animation); // targetProgressに達したらアニメーションを停止
                setProgress(targetProgress); // 最後のテキスト表示を正しく設定
            }
            currentProgress += step; // プログレスを増加
        }, interval);