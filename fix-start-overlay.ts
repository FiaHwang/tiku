import fs from "fs";

const fixMobile = () => {
    let content = fs.readFileSync('mobile/shiti_jiexi.html', 'utf8');
    
    // Add start-overlay HTML
    const searchHtml = `<div class="trial-overlay" id="trial-overlay">`;
    const replaceHtml = `<div class="start-overlay" id="start-overlay">
                    <h3 style="color: #f5222d; margin-bottom: 8px;">会员专享</h3>
                    <p style="margin-bottom: 20px;">支持试看</p>
                    <button class="btn" id="start-trial-btn" style="background-color: #1890ff;">开始试看</button>
                </div>
                <div class="trial-overlay" id="trial-overlay">`;
    
    if (!content.includes('id="start-overlay"')) {
        content = content.replace(searchHtml, replaceHtml);
    }
    
    // Add CSS for start-overlay
    const searchCSS = `.trial-overlay {`;
    const replaceCSS = `.start-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.85);
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #fff;
            z-index: 10;
            padding: 20px;
            text-align: center;
        }

        .start-overlay.active {
            display: flex;
        }

        .trial-overlay {`;
    
    if (!content.includes('.start-overlay {')) {
        content = content.replace(searchCSS, replaceCSS);
    }
    
    // Fix JS
    const searchJS = `trialOverlay.classList.remove('active');
                videoElement.currentTime = 0;`;
    const replaceJS = `trialOverlay.classList.remove('active');
                videoElement.currentTime = 0;
                // 显示开始试看遮罩
                const startOverlay = document.getElementById('start-overlay');
                if (startOverlay) {
                    startOverlay.classList.add('active');
                }
                videoElement.pause();`;
    
    if (!content.includes('startOverlay.classList.add(\'active\');')) {
        content = content.replace(searchJS, replaceJS);
    }
    
    const searchJS2 = `// 视频播放进度监控 (试看逻辑)`;
    const replaceJS2 = `// 试看按钮点击事件
        const startTrialBtn = document.getElementById('start-trial-btn');
        if (startTrialBtn) {
            startTrialBtn.addEventListener('click', () => {
                const startOverlay = document.getElementById('start-overlay');
                if (startOverlay) {
                    startOverlay.classList.remove('active');
                }
                videoElement.play();
            });
        }
        
        // 视频播放进度监控 (试看逻辑)`;
    if (!content.includes('startTrialBtn.addEventListener')) {
        content = content.replace(searchJS2, replaceJS2);
    }

    fs.writeFileSync('mobile/shiti_jiexi.html', content);
};

const fixPC = () => {
    let content = fs.readFileSync('pc/shiti_jiexi_pc.html', 'utf8');
    
    // Add start-overlay HTML (the PC has inline styles for trial-overlay, let's match)
    const searchHtml = `<div class="trial-overlay" id="trial-overlay"`;
    const replaceHtml = `<div class="start-overlay" id="start-overlay" style="display: none; flex-direction: column; align-items: center; justify-content: center; color: #fff; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.85); z-index: 10;">
                    <h3 style="font-size: 24px; color: #f5222d; margin-bottom: 10px;">会员专享</h3>
                    <p style="font-size: 16px; margin-bottom: 20px;">支持试看</p>
                    <button class="action-btn" id="start-trial-btn-pc" style="background-color: #1890ff; color: white; border: none; padding: 10px 20px; border-radius: 20px; cursor: pointer; font-size: 16px;">开始试看</button>
                </div>
                <div class="trial-overlay" id="trial-overlay"`;
    
    if (!content.includes('id="start-overlay"')) {
        content = content.replace(searchHtml, replaceHtml);
    }
    
    // Fix JS
    const searchJS = `document.querySelectorAll('.video-analysis').forEach(el => {
            el.addEventListener('click', () => {
                videoModal.classList.add('active');
                videoElement.play();`;
    const replaceJS = `document.querySelectorAll('.video-analysis').forEach(el => {
            el.addEventListener('click', () => {
                videoModal.classList.add('active');
                const startOverlay = document.getElementById('start-overlay');
                if(startOverlay) startOverlay.style.display = 'flex';
                const trialOverlay = document.getElementById('trial-overlay');
                if(trialOverlay) trialOverlay.style.display = 'none';
                videoElement.currentTime = 0;
                videoElement.pause();`;
    
    if (!content.includes('startOverlay.style.display = \'flex\';')) {
        content = content.replace(searchJS, replaceJS);
    }
    
    const searchJS2 = `// 视频试看逻辑`;
    const replaceJS2 = `// 试看按钮点击事件
        const startTrialBtnPc = document.getElementById('start-trial-btn-pc');
        if(startTrialBtnPc) {
            startTrialBtnPc.addEventListener('click', () => {
                const startOverlay = document.getElementById('start-overlay');
                if(startOverlay) startOverlay.style.display = 'none';
                videoElement.play();
            });
        }
        
        // 视频试看逻辑`;
    if (!content.includes('startTrialBtnPc.addEventListener')) {
        content = content.replace(searchJS2, replaceJS2);
    }

    fs.writeFileSync('pc/shiti_jiexi_pc.html', content);
}

fixMobile();
fixPC();
console.log("Done All");
