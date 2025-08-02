// DOM Elements
const shareModal = document.getElementById('shareModal');
const closeModal = document.querySelector('.close');

// Event Listeners
closeModal.addEventListener('click', () => {
    shareModal.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === shareModal) {
        shareModal.style.display = 'none';
    }
});

// Download vCard function
function downloadVCard() {
    const vCardData = `BEGIN:VCARD
VERSION:3.0
FN:Keval Chauhan
ORG:Web Developer
TEL;TYPE=CELL:+919429806587
EMAIL:keval.chauhan@email.com
URL:https://keval.live
URL:https://linkedin.com/in/keval-s-chauhan
URL:https://github.com/soul059
NOTE:Full Stack Web Developer specializing in HTML, CSS, JavaScript, React, Node.js, and MongoDB. Portfolio: https://keval.live
END:VCARD`;

    const blob = new Blob([vCardData], { type: 'text/vcard' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'keval-chauhan-contact.vcf';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
    
    // Show success message
    showNotification('Contact saved successfully!', 'success');
}

// Share card function
function shareCard() {
    shareModal.style.display = 'block';
}

// Share to WhatsApp
function shareToWhatsApp() {
    const message = encodeURIComponent(`Hi! I'm Keval Chauhan, a Web Developer. 

📱 Mobile: +91 9429806587
🌐 Portfolio: https://keval.live
💻 Skills: HTML, CSS, JavaScript, React, Node.js, MongoDB
🔗 LinkedIn: linkedin.com/in/keval-s-chauhan
🔗 GitHub: github.com/soul059

Let's connect and build something amazing together!`);
    
    window.open(`https://wa.me/?text=${message}`, '_blank');
    shareModal.style.display = 'none';
}

// Share via Email
function shareToEmail() {
    const subject = encodeURIComponent('Keval Chauhan - Web Developer Contact');
    const body = encodeURIComponent(`Hi,

I'd like to share Keval Chauhan's contact information with you:

Name: Keval Chauhan
Position: Web Developer
Mobile: +91 9429806587
Portfolio: https://keval.live
Skills: HTML, CSS, JavaScript, React, Node.js, MongoDB

LinkedIn: https://linkedin.com/in/keval-s-chauhan
GitHub: https://github.com/soul059

Best regards!`);
    
    window.open(`mailto:?subject=${subject}&body=${body}`, '_blank');
    shareModal.style.display = 'none';
}

// Copy link function
function copyLink() {
    const currentUrl = window.location.href;
    
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(currentUrl).then(() => {
            showNotification('Link copied to clipboard!', 'success');
        }).catch(() => {
            fallbackCopyTextToClipboard(currentUrl);
        });
    } else {
        fallbackCopyTextToClipboard(currentUrl);
    }
    
    shareModal.style.display = 'none';
}

// Fallback copy function for older browsers
function fallbackCopyTextToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.top = '0';
    textArea.style.left = '0';
    textArea.style.position = 'fixed';
    textArea.style.opacity = '0';
    
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        document.execCommand('copy');
        showNotification('Link copied to clipboard!', 'success');
    } catch (err) {
        showNotification('Failed to copy link', 'error');
    }
    
    document.body.removeChild(textArea);
}

// Show notification function
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Add notification styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 20px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 1001;
        animation: slideInRight 0.3s ease;
        max-width: 300px;
        word-wrap: break-word;
    `;
    
    // Set background color based on type
    switch (type) {
        case 'success':
            notification.style.background = 'linear-gradient(135deg, #28a745, #20c997)';
            break;
        case 'error':
            notification.style.background = 'linear-gradient(135deg, #dc3545, #e74c3c)';
            break;
        default:
            notification.style.background = 'linear-gradient(135deg, #667eea, #764ba2)';
    }
    
    // Add animation keyframes
    if (!document.querySelector('#notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            @keyframes slideInRight {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOutRight {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(notification);
    
    // Auto remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Add hover effects to contact items
document.addEventListener('DOMContentLoaded', () => {
    const contactItems = document.querySelectorAll('.contact-item');
    
    contactItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            item.style.transform = 'translateX(5px)';
            item.style.transition = 'transform 0.3s ease';
        });
        
        item.addEventListener('mouseleave', () => {
            item.style.transform = 'translateX(0)';
        });
        
        // Add click functionality for different contact types
        item.addEventListener('click', () => {
            const text = item.querySelector('span').textContent;
            const icon = item.querySelector('i');
            
            if (icon.classList.contains('fa-phone')) {
                // Phone number - copy and show dial option on mobile
                if (navigator.clipboard && window.isSecureContext) {
                    navigator.clipboard.writeText(text).then(() => {
                        showNotification(`Phone number copied: ${text}`, 'success');
                    });
                }
                if (/Mobi|Android/i.test(navigator.userAgent)) {
                    setTimeout(() => {
                        if (confirm('Would you like to dial this number?')) {
                            window.open(`tel:${text}`, '_self');
                        }
                    }, 1000);
                }
            } else if (icon.classList.contains('fa-envelope')) {
                // Email - open email client
                window.open(`mailto:${text}`, '_blank');
                showNotification('Opening email client...', 'info');
            } else if (icon.classList.contains('fa-globe')) {
                // Portfolio website - open in new tab
                window.open(`https://${text}`, '_blank');
                showNotification('Opening portfolio website...', 'info');
            } else if (icon.classList.contains('fa-linkedin')) {
                // LinkedIn - open in new tab
                window.open(`https://${text}`, '_blank');
                showNotification('Opening LinkedIn profile...', 'info');
            } else if (icon.classList.contains('fa-github')) {
                // GitHub - open in new tab
                window.open(`https://${text}`, '_blank');
                showNotification('Opening GitHub profile...', 'info');
            } else {
                // Default - copy to clipboard
                if (navigator.clipboard && window.isSecureContext) {
                    navigator.clipboard.writeText(text).then(() => {
                        showNotification(`Copied: ${text}`, 'success');
                    });
                } else {
                    fallbackCopyTextToClipboard(text);
                }
            }
        });
    });
    
    // Add animation to skill tags
    const skillTags = document.querySelectorAll('.skill-tag');
    skillTags.forEach((tag, index) => {
        tag.style.animationDelay = `${index * 0.1}s`;
        tag.style.animation = 'fadeInUp 0.6s ease forwards';
    });
    
    // Add fade in animation keyframes
    if (!document.querySelector('#animation-styles')) {
        const style = document.createElement('style');
        style.id = 'animation-styles';
        style.textContent = `
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        `;
        document.head.appendChild(style);
    }
});

// Add keyboard shortcuts
document.addEventListener('keydown', (event) => {
    // ESC to close modal
    if (event.key === 'Escape' && shareModal.style.display === 'block') {
        shareModal.style.display = 'none';
    }
    
    // Ctrl/Cmd + S to download vCard
    if ((event.ctrlKey || event.metaKey) && event.key === 's') {
        event.preventDefault();
        downloadVCard();
    }
    
    // Ctrl/Cmd + Shift + S to share
    if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.key === 'S') {
        event.preventDefault();
        shareCard();
    }
});

// Add loading animation
window.addEventListener('load', () => {
    const card = document.querySelector('.business-card');
    card.style.opacity = '0';
    card.style.transform = 'translateY(50px) rotateX(10deg)';
    card.style.transition = 'all 0.8s ease';
    
    setTimeout(() => {
        card.style.opacity = '1';
        card.style.transform = 'translateY(0) rotateX(0deg)';
    }, 100);
    
    // Add responsive touch events for mobile
    if ('ontouchstart' in window) {
        addTouchSupport();
    }
});

// Add touch support for mobile devices
function addTouchSupport() {
    const contactItems = document.querySelectorAll('.contact-item');
    const skillTags = document.querySelectorAll('.skill-tag');
    
    // Add touch feedback for contact items
    contactItems.forEach(item => {
        item.addEventListener('touchstart', () => {
            item.style.transform = 'translateX(5px)';
        });
        
        item.addEventListener('touchend', () => {
            setTimeout(() => {
                item.style.transform = 'translateX(0)';
            }, 100);
        });
    });
    
    // Add touch feedback for skill tags
    skillTags.forEach(tag => {
        tag.addEventListener('touchstart', () => {
            tag.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        tag.addEventListener('touchend', () => {
            setTimeout(() => {
                tag.style.transform = 'translateY(0) scale(1)';
            }, 100);
        });
    });
}

// Handle orientation changes
window.addEventListener('orientationchange', () => {
    // Adjust layout after orientation change
    setTimeout(() => {
        const card = document.querySelector('.business-card');
        card.style.transition = 'all 0.3s ease';
    }, 500);
});

// Handle window resize for responsive adjustments
window.addEventListener('resize', debounce(() => {
    adjustResponsiveElements();
}, 250));

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Adjust elements based on screen size
function adjustResponsiveElements() {
    const screenWidth = window.innerWidth;
    const floatingElements = document.querySelectorAll('.floating-circle, .floating-square, .floating-triangle');
    
    // Hide floating elements on small screens for better performance
    if (screenWidth <= 480) {
        floatingElements.forEach(element => {
            element.style.display = 'none';
        });
    } else {
        floatingElements.forEach(element => {
            element.style.display = 'block';
        });
    }
}

// Add parallax effect to floating elements
document.addEventListener('mousemove', (event) => {
    const mouseX = event.clientX / window.innerWidth;
    const mouseY = event.clientY / window.innerHeight;
    
    const floatingElements = document.querySelectorAll('.floating-circle, .floating-square, .floating-triangle');
    
    floatingElements.forEach((element, index) => {
        const speed = (index + 1) * 0.5;
        const x = mouseX * speed * 10;
        const y = mouseY * speed * 10;
        
        element.style.transform += ` translate(${x}px, ${y}px)`;
    });
});

// Add QR code functionality (placeholder)
document.querySelector('.qr-code').addEventListener('click', () => {
    showNotification('QR Code feature coming soon!', 'info');
});

// Add print functionality
function printCard() {
    window.print();
}

// Add context menu for additional options
document.querySelector('.business-card').addEventListener('contextmenu', (event) => {
    event.preventDefault();
    
    // Create custom context menu
    const contextMenu = document.createElement('div');
    contextMenu.innerHTML = `
        <div style="
            position: fixed;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            padding: 8px 0;
            z-index: 1002;
            min-width: 150px;
            left: ${event.pageX}px;
            top: ${event.pageY}px;
        ">
            <div class="context-item" onclick="downloadVCard()">💾 Save Contact</div>
            <div class="context-item" onclick="shareCard()">📤 Share Card</div>
            <div class="context-item" onclick="printCard()">🖨️ Print Card</div>
        </div>
    `;
    
    // Add styles for context menu items
    const style = document.createElement('style');
    style.textContent = `
        .context-item {
            padding: 8px 16px;
            cursor: pointer;
            font-size: 14px;
            color: #2c3e50;
            transition: background 0.2s ease;
        }
        .context-item:hover {
            background: #f8f9fa;
        }
    `;
    document.head.appendChild(style);
    
    document.body.appendChild(contextMenu);
    
    // Remove context menu when clicking elsewhere
    const removeContextMenu = () => {
        if (contextMenu.parentNode) {
            contextMenu.parentNode.removeChild(contextMenu);
        }
        document.removeEventListener('click', removeContextMenu);
    };
    
    setTimeout(() => {
        document.addEventListener('click', removeContextMenu);
    }, 100);
});
