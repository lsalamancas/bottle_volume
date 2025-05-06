---
marp: true
theme: default
paginate: true
header: "Bottle Volume Calculation"
footer: "Numerical Methods in Image Processing"
---

# 📄 Bottle Volume Estimation Using Numerical Methods
### Luis Salamanca, Daniel Zarate - 2025

---

# 📌 Abstract
- Estimating the volume of a Coca-Cola bottle using image processing.
- Three numerical integration methods were used:
  - **Simpson's Rule**
  - **Trapezoidal Rule**
  - **Rectangle Method**
- Simpson's Rule provided the closest estimate to the actual volume (330ml).

---

# 📖 Introduction
- Measuring irregular shapes can be challenging.
- Computational methods provide a practical way to approximate volumes.
- The contour of the bottle is extracted and used for numerical integration.

---

# 🏗 Numerical Integration Methods
### Simpson’s Rule
$$
\int_{a}^{b} f(x) dx \approx \frac{h}{3} \sum_{i=0}^{n} \left[ f(x_i) + 4f(x_{i+1}) + f(x_{i+2}) \right]
$$

### Trapezoidal Rule
$$
\int_{a}^{b} f(x) dx \approx \frac{h}{2} \sum_{i=0}^{n} \left[ f(x_i) + f(x_{i+1}) \right]
$$

### Rectangle Method
$$
\int_{a}^{b} f(x) dx \approx \sum_{i=0}^{n} f(x_i) \cdot \Delta x
$$

---

# 🔎 Image Processing Steps

<style>
.columns {
  display: flex;
}
.column {
  flex: 1;
  padding: 10px;
}
</style>

<div class="columns">
  <div class="column">
    ### 1. Convert to grayscale  
    ### 2. Apply Gaussian blur
  </div>
  <div class="column">
    ### 3. Perform binary thresholding  
    ### 4. Extract contour using OpenCV
  </div>
</div>

---
* 1. Convert to grayscal

**2. Apply Gaussian blur**
**3. Perform binary thresholding**  
**4. Extract contour using OpenCV**
---
```python
gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv.threshold(blurred, 175, 255, cv.THRESH_BINARY_INV)
contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(self.image, contours, -1, (0, 255, 0), 3)
```
---
# 🔁 Contour Extraction & Scaling

### Extracted contour rotated to align axes.

Converted pixel measurements to centimeters.

```python
scale_to_mm = self.bottle_heigh / h
black_points = np.column_stack(np.where(img_rotated < 1))
self.function_cm = scale_to_mm * black_points[:, 0:2]
```

---
# 📊 Results

| **Method**         | **Estimated Volume (ml)** | **Error (ml)** | **RMS Contribution** |
|--------------------|-------------------------|--------------|--------------------|
| **Simpson's Rule** | 322 ml                   | -8 ml       | 64                |
| **Trapezoidal Rule** | 480 ml                   | +150 ml      | 22500             |
| **Rectangle Method** | 390 ml                   | +60 ml       | 3600              |
| **Actual Bottle**   | 330 ml                   | N/A         | N/A               |

✅ Simpson’s Rule was the most accurate.
✅ **Total RMS Error** = **93.4 ml**

---
# 🎯 Conclusion

### 1.Numerical methods allow estimating complex shapes.

### 2.Simpson’s Rule is the best approximation method.

### 3.Potential applications in manufacturing, quality control, and automation.

# 📌 Future Work

### Improve contour detection accuracy, it does not work properly in png images or transparent bottles.

### Test more integration methods.

### Apply this technique to different bottle shapes.