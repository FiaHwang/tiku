const fs = require('fs');

const fixMobile = () => {
    let content = fs.readFileSync('mobile/shiti_jiexi.html', 'utf8');
    const search = `<div class="video-analysis">
                            <div>
                                <i class="fas fa-play-circle"></i>
                                <span>视频解析</span>
                            </div>
                        </div>`;
    const replace = `<div class="video-analysis" style="display:flex; justify-content: space-between; align-items: center;">
                            <div>
                                <i class="fas fa-play-circle"></i>
                                <span>视频解析</span>
                            </div>
                            <div style="display: flex; gap: 6px;">
                                <span style="font-size: 10px; padding: 2px 6px; background-color: #fff1f0; color: #f5222d; border-radius: 10px; border: 1px solid #ffa39e;">会员专享</span>
                                <span style="font-size: 10px; padding: 2px 6px; background-color: #e6f7ff; color: #1890ff; border-radius: 10px; border: 1px solid #91d5ff;">支持试看</span>
                            </div>
                        </div>`;
    content = content.replace(new RegExp(search.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&").replace(/\s+/g, '\\s*'), 'g'), replace);
    fs.writeFileSync('mobile/shiti_jiexi.html', content);
};

const fixPC = () => {
    let content = fs.readFileSync('pc/shiti_jiexi_pc.html', 'utf8');
    const search = `<div class="video-analysis" style="margin-bottom: 16px; padding: 12px; background-color: #f9f9f9; border-radius: 4px; border-left: 4px solid #1890ff;">
                                        <div style="display: flex; align-items: center; cursor: pointer;">
                                            <i class="fas fa-play-circle" style="font-size: 24px; color: #1890ff; margin-right: 12px;"></i>
                                            <span style="font-weight: 500;">视频解析</span>
                                        </div>
                                    </div>`;
    const replace = `<div class="video-analysis" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding: 12px; background-color: #f9f9f9; border-radius: 4px; border-left: 4px solid #1890ff; cursor: pointer;">
                                        <div style="display: flex; align-items: center;">
                                            <i class="fas fa-play-circle" style="font-size: 24px; color: #1890ff; margin-right: 12px;"></i>
                                            <span style="font-weight: 500;">视频解析</span>
                                        </div>
                                        <div style="display: flex; gap: 8px;">
                                            <span style="font-size: 12px; padding: 2px 8px; background-color: #fff1f0; color: #f5222d; border-radius: 2px; border: 1px solid #ffa39e;">会员专享</span>
                                            <span style="font-size: 12px; padding: 2px 8px; background-color: #e6f7ff; color: #1890ff; border-radius: 2px; border: 1px solid #91d5ff;">支持试看</span>
                                        </div>
                                    </div>`;
    content = content.replace(new RegExp(search.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&").replace(/\s+/g, '\\s*'), 'g'), replace);
    fs.writeFileSync('pc/shiti_jiexi_pc.html', content);
};

fixMobile();
fixPC();
console.log("Done");
