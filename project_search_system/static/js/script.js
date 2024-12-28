const progressRing = document.querySelector('.progress-ring__circle');
const elment = document.getElementById('percentage-display-sentence').textContent;
const progressText = document.querySelector('.progress-text');
const circumference = 2 * Math.PI * 70; 
let currentProgress = 0; 
const interval = 50; 
const step = 1; 
const targetProgress = Number(elment); 

function setProgress(percent) {
    const offset = circumference - percent / 100 * circumference;
    progressRing.style.strokeDasharray = `${circumference} ${circumference}`;
    progressRing.style.strokeDashoffset = offset;
    progressText.textContent = `${percent}%`; 
}

const animation = setInterval(() => {
    setProgress(currentProgress);
    if (currentProgress >= targetProgress) {
        clearInterval(animation); 
        setProgress(targetProgress); 
    }
    currentProgress += step; 
}, interval);