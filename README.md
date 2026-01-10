# Mall-Customer-Segmentation
# **AVM Müşteri Segmentasyonu Analizi (K-Means Clustering)**

## **1. Proje Özeti ve İş Problemi**

#### Bu projede, büyük bir alışveriş merkezi (AVM) yönetiminin pazarlama bütçesini daha verimli kullanabilmesi için makine öğrenmesi tabanlı müşteri segmentasyonu gerçekleştirilmiştir. Amaç, benzer harcama davranışlarına sahip müşterileri gruplamak ve her segmente özel pazarlama stratejileri geliştirilmesini sağlamaktır.

#### **Veri seti Kaggle'dan alınmıştır.**

**Veri seti:** https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python/data?select=Mall_Customers.csv

### Problem Tanımı 

#### AVM yönetiminin elinde aşağıdaki müşteri bilgileri bulunmaktadır:

* Gender

* Age

* Annual Income (Yıllık Gelir)

* Spending Score (Harcama Skoru – 1-100)

#### Ancak:

* Müşterilerin nasıl kategorize edileceği bilinmemektedir.

* Her müşteriye aynı kampanyayı yapmak maliyetlidir.

#### Hedef: Benzer özelliklere sahip müşterileri kümeleme (clustering) yöntemiyle gruplamak ve:

* Zengin ama az harcayanlar

* Orta gelirli ama çok harcayanlar

* Sadık müşteriler

* Düşük gelir – düşük harcama grubu

gibi segmentler oluşturmak.

### Kullanılan Kütüphaneler

* **Pandas:** Veri setinin yüklenmesi, ön işlenmesi ve tablo tabanlı veri analizinin gerçekleştirilmesi için kullanılmıştır.

* **NumPy:** Sayısal hesaplamalar ve makine öğrenmesi algoritmalarının matematiksel altyapısını sağlamak amacıyla kullanılmıştır.

* **Matplotlib:** Veri analizi ve model sonuçlarının grafikler aracılığıyla görselleştirilmesi için kullanılmıştır.

* **Seaborn:** Kümeleme sonuçlarının daha anlaşılır ve estetik biçimde görselleştirilmesi için kullanılmıştır.

* **Scikit-learn:** Müşteri segmentasyonu için K-Means kümeleme modeli ve veri ölçekleme işlemlerinin uygulanması amacıyla kullanılmıştır.

