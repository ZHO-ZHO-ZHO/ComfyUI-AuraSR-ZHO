

![ASR封面图](https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/assets/140084057/b06dc082-ab4b-4aec-8959-7ebd8bfd1b0c)



# AURASR IN COMFYUI

Unofficial implementation of [AuraSR](https://github.com/fal-ai/aura-sr) in ComfyUI for img & video




https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/assets/140084057/a8458046-f379-40f0-8703-28f58232c874




## 项目介绍 | Info

- 对 [AuraSR](https://github.com/fal-ai/aura-sr) 的非官方实现

- AuraSR：基于 GigaGAN 的 4x 超分模型，速度快，效果还可以（针对细节较好的原图效果好）
  
- 版本：V1.0 同时支持 图像 和 视频 放大



## 节点说明 | Features

- AuraSR 模型加载 | 🔎AuraSR Model
    - 需手动下载 [AuraSR 模型](https://huggingface.co/fal/AuraSR/resolve/main/model.safetensors?download=true) 放入 `/ComfyUI/models/aurasr` 中
    
- 放大图像 | 🔎AuraSR(image)
    
- 放大视频| 🔎AuraSR(video)
    - 若存在 RGBA 且输出配合 Video Helper Suite 插件使用，则需要使用 ComfyUI 自带的 Split Image with Alpha 节点去除 Alpha 通道
 
 ![screenshot-20240711-003630](https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/assets/140084057/42203b40-0bcb-4fe0-ad4a-86537173f4c7)


## 安装 | Install

- 推荐使用管理器 ComfyUI Manager 安装

- 手动安装：
    1. `cd custom_nodes`
    2. `git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO.git`
    3. 重启 ComfyUI


## 工作流 | Workflows

V1.0

  - [V1.0 AuraSR img](https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/blob/main/AURASR%20WORKFLOWS/V1.0%20APISR%20img%E3%80%90Zho%E3%80%91.json)

    ![screenshot-20240711-005201](https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/assets/140084057/fbcf5f03-dd31-4e12-bad8-8b0a9145da7e)


  - [V1.0 AuraSR video](https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/blob/main/AURASR%20WORKFLOWS/V1.0%20APISR%20video%E3%80%90Zho%E3%80%91.json)
    
    ![screenshot-20240711-005024](https://github.com/ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO/assets/140084057/6475c976-4ac3-4cc7-95c0-5da3c04098a4)



## 更新日志

- 20240710

  V1.0 同时支持 图像 与 视频 的放大
  
  创建项目
  

## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-AuraSR-ZHO&Date)


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

[AuraSR](https://github.com/fal-ai/aura-sr)
