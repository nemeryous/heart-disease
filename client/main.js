document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });

            // Close mobile menu if open
            document.getElementById('navMenu').classList.remove('active');
        }
    });
});

document.getElementById('menuToggle').addEventListener('click', function () {
    document.getElementById('navMenu').classList.toggle('active');
});

const heartForm = document.getElementById('heartForm');
const resultsSection = document.getElementById('results');
const progressCircle = document.getElementById('progressCircle');
const riskPercentage = document.getElementById('riskPercentage');
const riskLevel = document.getElementById('riskLevel');
const riskFactorsList = document.getElementById('riskFactorsList');
const suggestionsList = document.getElementById('suggestionsList');
const resetBtn = document.getElementById('resetBtn');

heartForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = {
        age: parseInt(document.getElementById('age').value),
        sex: parseInt(document.getElementById('sex').value),
        cp: parseInt(document.getElementById('cp').value),
        trestbps: parseInt(document.getElementById('trestbps').value),
        chol: parseInt(document.getElementById('chol').value),
        fbs: parseInt(document.getElementById('fbs').value),
        restecg: parseInt(document.getElementById('restecg').value),
        thalach: parseInt(document.getElementById('thalach').value),
        exang: parseInt(document.getElementById('exang').value),
        oldpeak: parseFloat(document.getElementById('oldpeak').value),
        slope: parseInt(document.getElementById('slope').value),
        ca: parseInt(document.getElementById('ca').value),
        thal: parseInt(document.getElementById('thal').value)
    };

    try {
        resultsSection.style.display = 'block';
        resultsSection.innerHTML = '<div class="loading">Đang phân tích...</div>';
        console.log('Form Data:', formData);

        const response = await fetch('http://localhost:8000/api/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || 'Có lỗi xảy ra khi dự đoán');
        }

        const resultsHTML = `
            <div class="risk-level" id="riskLevel">
                <span class="${result.prediction === 1 ? 'high' : 'low'}">${result.prediction === 1 ? 'Có dấu hiệu bệnh tim mạch' : 'Không có dấu hiệu bệnh tim mạch'}</span>
                <span>${result.confidence}</span>
            </div>

            <div class="suggestions">
                <h3>Gợi ý</h3>
                <div id="suggestionsList">
                    <div class="suggestion-item">
                        <div class="suggestion-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M3 12h18M3 6h18M3 18h18"></path>
                            </svg>
                        </div>
                        <div>Tư vấn với bác sĩ để đánh giá tình trạng sức khỏe tim mạch của bạn</div>
                    </div>
                    ${result.prediction === 1 ? `
                        <div class="suggestion-item">
                            <div class="suggestion-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                                    <line x1="9" y1="9" x2="9.01" y2="9"></line>
                                    <line x1="15" y1="9" x2="15.01" y2="9"></line>
                                </svg>
                            </div>
                            <div>Thực hiện chế độ ăn lành mạnh và tập thể dục đều đặn</div>
                        </div>
                    ` : ''}
                    <div class="suggestion-item">
                        <div class="suggestion-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                            </svg>
                        </div>
                        <div>Kiểm tra sức khỏe định kỳ để theo dõi các chỉ số tim mạch</div>
                    </div>
                </div>
            </div>

            <button class="btn-reset" id="resetBtn">Làm Lại</button>
        `;

        resultsSection.innerHTML = resultsHTML;

        const circumference = 2 * Math.PI * 90;
        const riskPercentage = result.prediction === 1 ? 75 : 25;
        const offset = circumference - (riskPercentage / 100) * circumference;
        progressCircle.style.strokeDasharray = circumference;
        progressCircle.style.strokeDashoffset = offset;
        progressCircle.style.stroke = result.prediction === 1 ?
            getComputedStyle(document.documentElement).getPropertyValue('--red') || "#E74C3C" :
            getComputedStyle(document.documentElement).getPropertyValue('--green') || "#2ECC71";

        setTimeout(() => {
            resultsSection.classList.add('active');
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);

        document.getElementById('resetBtn').addEventListener('click', function () {
            heartForm.reset();
            resultsSection.classList.remove('active');
            setTimeout(() => {
                resultsSection.style.display = 'none';
            }, 300);
            document.querySelector('.form-title').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });

    } catch (error) {
        console.error('Error:', error);
        resultsSection.innerHTML = `<div class="error">${error.message}</div>`;
    }
});

progressCircle.style.strokeDasharray = 2 * Math.PI * 90;