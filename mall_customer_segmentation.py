# Kütüphanelerin Yüklenmesi ve Veri Seti

# Kütüphaneleri Yükleme 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings('ignore')

# Veriyi Yükleme
df = pd.read_csv('data/Mall_Customers.csv')

# Keşifsel Veri Analizi (EDA)
# Genel Bakış
print("--- Veri Seti Bilgisi ---")
print(df.info())

print("\n--- İlk 5 Satır ---")
print(df.head())

# İstatistiksel Özet
print("\n--- İstatistiksel Özet ---")
print(df.describe().T)

# Eksik Değer Kontrolü
print("\n--- Eksik Değer Sayısı ---")
print(df.isnull().sum())


#Görsel Analiz: Değişkenlerin Dağılımı
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True, color='blue')
plt.title('Yaş Dağılımı')

plt.subplot(1, 3, 2)
sns.histplot(df['Annual Income (k$)'], kde=True, color='green')
plt.title('Yıllık Gelir Dağılımı')

plt.subplot(1, 3, 3)
sns.histplot(df['Spending Score (1-100)'], kde=True, color='red')
plt.title('Harcama Skoru Dağılımı')

plt.show()

#Özellikler Arası Korelasyon Analizi
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Özellikler Arası Korelasyon Isı Haritası')
plt.show()

# Feature Engineering (Özellik Mühendisliği)
# Kümeleme için kullanılacak özelliklerin seçilmesi
# Analizi zenginleştirmek için Yaş, Gelir ve Skoru dahil ediyoruz
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Standartlaştırma (Verileri 0-1 aralığına/benzer ölçeğe çekme)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Veri ön işleme tamamlandı ve ölçeklendirildi.")

# Model Seçimi ve Dirsek (Elbow) Yöntemi
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='purple')
plt.title('Optimal Küme Sayısı (Dirsek Yöntemi)')
plt.xlabel('Küme Sayısı')
plt.ylabel('WCSS (Küme İçi Hata)')
plt.show()

# Modelin Uygulanması ve 3D Görselleştirme
# Final modelin kurulması
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42, n_init=10)
df['Segment'] = kmeans.fit_predict(X_scaled)

# Segment sayılarını kontrol etme
print(df['Segment'].value_counts())

# 3D İnteraktif Görselleştirme (Plotly)
fig = px.scatter_3d(df, 
                    x='Age', 
                    y='Annual Income (k$)', 
                    z='Spending Score (1-100)',
                    color='Segment',
                    title='AVM Müşteri Segmentasyonu (3 Boyutlu)',
                    opacity=0.8,
                    color_continuous_scale='Viridis')

fig.show()

# İş Analizi ve Strateji Önerileri
# Her grubun özelliklerini inceleyelim
segment_analysis = df.groupby('Segment')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
print(segment_analysis)
