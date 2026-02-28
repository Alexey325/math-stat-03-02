import numpy as np
import matplotlib.pyplot as plt

# ЗАДАНИЕ: Первичная обработка выборки

data = np.loadtxt('variant_7.csv', delimiter=',')

n = len(data)
print(f"Объём выборки: n = {n}")

# ШАГ 1: Вариационный ряд

sorted_data = np.sort(data)

print(f"\nПервые 5 значений вариационного ряда:")
print(*sorted_data[:5])

print(f"\nПоследние 5 значений вариационного ряда:")
print(*sorted_data[-5:])

# ШАГ 2: Выборочные оценки

x_bar = np.mean(data)
s2 = np.var(data, ddof=1)
s = np.std(data, ddof=1)
median = np.median(data)
x_min = np.min(data)
x_max = np.max(data)

print(f"\nВыборочные оценки:")
print(f"  Среднее:      x̄ = {x_bar:.4f}")
print(f"  Дисперсия:    s² = {s2:.4f}")
print(f"  Ст. откл.:    s = {s:.4f}")
print(f"  Медиана:      x̃ = {median:.4f}")
print(f"  Размах:       [{x_min:.1f}, {x_max:.1f}]")
print()

# ШАГ 3: Правило Скотта и гистограмма

h = 3.5 * s * n**(-1/3)

k = int(np.ceil((x_max - x_min) / h))

print(f"Правило Скотта:")
print(f"  Ширина интервала: h = {h:.2f}")
print(f"  Число интервалов: k = {k}")

counts, bin_edges = np.histogram(data, bins=k)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# а) с числом интервалов по Скотту
axes[0].hist(data, bins=k, edgecolor='black', alpha=0.7, color='skyblue')
axes[0].axvline(x=x_bar, color='red', linestyle='--', linewidth=2, label=f'Среднее = {x_bar:.2f}')
axes[0].set_title(f'Гистограмма (по Скотту, k={k})')
axes[0].set_xlabel('Значения')
axes[0].set_ylabel('Частота')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# б) с фиксированным числом интервалов = 5
axes[1].hist(data, bins=5, edgecolor='black', alpha=0.7, color='lightcoral')
axes[1].axvline(x=x_bar, color='red', linestyle='--', linewidth=2, label=f'Среднее = {x_bar:.2f}')
axes[1].set_title('Гистограмма (фиксированное k=5)')
axes[1].set_xlabel('Значения')
axes[1].set_ylabel('Частота')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()

# ШАГ 4: Полигон частот

plt.figure(2, figsize=(10, 6))

plt.plot(bin_centers, counts, 'o-', color='orange', linewidth=2, markersize=8,
         markerfacecolor='orange', markeredgecolor='darkorange', markeredgewidth=1.5,
         label='Полигон частот')

plt.title('Полигон частот', fontsize=14, fontweight='bold')
plt.xlabel('Значение x', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend()

for i, (center, count) in enumerate(zip(bin_centers, counts)):
    plt.text(center, count + 0.1, str(int(count)), ha='center', va='bottom', fontsize=10)

plt.ylim(0, max(counts) + 1)
plt.xlim(min(bin_centers) - 1, max(bin_centers) + 1)

plt.tight_layout()

# Таблица частот
print("\nТаблица частот (по интервалам Скотта):")
print("-" * 40)
print("  Интервал          | Середина | Частота")
print("-" * 40)
for i in range(len(bin_centers)):
    print(f"  [{bin_edges[i]:.1f}, {bin_edges[i+1]:.1f}) | {bin_centers[i]:.1f}      | {counts[i]}")
print("-" * 40)

plt.show()

# # ШАГ 5: Эмпирическая функция распределения
# # -------------------------------------------------
# # ДОПОЛНИТЕ КОД:
# # Постройте график ЭФР с пунктирными вертикалями в точках скачков
# # и точками на горизонтальных участках
#
# # -------------------------------------------------
# # ШАГ 6: Сравнение с истинными параметрами
# # -------------------------------------------------
# # Истинные параметры вашего варианта:
# mu_true = ...   # подставьте μ для вышего варианта
# sigma2_true = ...  # подставьте σ² для вышего варианта
#
# print("Сравнение с истинными параметрами:")
# print(f"  Истинное μ = {mu_true}, выборочное x̄ = ...")
# print(f"  Истинное σ² = {sigma2_true}, выборочное s² = ...")
# print()
# print("Вопрос: Почему выборочные оценки отличаются от истинных параметров?")

