function renderChart(id, type, labels, data, label) {
  const ctx = document.getElementById(id).getContext("2d");
  new Chart(ctx, {
    type: type,
    data: {
      labels: labels,
      datasets: [{ label: label, data: data }]
    }
  });
}

fetch('/api/analises/clv')
  .then(res => res.json())
  .then(data => renderChart("clvChart", "bar", data.labels, data.values, "CLV"));

fetch('/api/analises/cluster')
  .then(res => res.json())
  .then(data => {
    const ctx = document.getElementById("clusterChart").getContext("2d");
    const grouped = {};
    for (let i = 0; i < data.labels.length; i++) {
      const label = data.labels[i];
      if (!grouped[label]) grouped[label] = [];
      grouped[label].push({ x: data.x[i], y: data.y[i] });
    }
    const datasets = Object.entries(grouped).map(([label, points]) => ({
      label: label,
      data: points,
      showLine: false,
      pointRadius: 5
    }));
    new Chart(ctx, {
      type: "scatter",
      data: { datasets: datasets }
    });
  });

fetch('/api/analises/campanhas')
  .then(res => res.json())
  .then(data => {
    renderChart("atributoChart", "bar", data.atributos, data.taxas_por_atributo, "Conversão por Atributo");
    renderChart("campanhaChart", "bar", data.campanhas, data.taxas_por_campanha, "Conversão por Campanha");
  });
