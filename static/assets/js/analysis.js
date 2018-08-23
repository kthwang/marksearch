 (function(window, document, $, undefined) {
            "use strict";
            $(function() {

                // ==============================================================
                // Traffic Sources Week
                // ==============================================================
                new Chartist.Line(
                    "#distance_total", {
                        labels: ["-3σ", "-2σ", "-1σ", "0", "1σ", "2σ", "3σ"],
                        series: {{ Distance.distance_total }}
                    }, {
                        high: 15,
                        low: 0,
                        showArea: true,
                        fullWidth: true,
                        axisY: {
                            onlyInteger: true,
                            offset: 20,

                        }
                    }
                );

                // ==============================================================
                // Traffic Sources Month
                // ==============================================================

                new Chartist.Line(
                    "#distance_same", {
                        labels: ["0", "4", "8", "12", "16", "20", "24", "28", "31"],
                        series: {{ Distance.distance_same }}
                    }, {
                        high: 15,
                        low: 0,
                        showArea: true,
                        fullWidth: true,

                        axisY: {
                            onlyInteger: true,
                            offset: 20,
                            labelInterpolationFnc: function(value) {
                                return value / 1 + "k";
                            }
                        }
                    }
                );

                // ==============================================================
                // Traffic Sources Year
                // ==============================================================

                new Chartist.Line(
                    "#distance_similar", {
                        labels: ["0", "4", "8", "12", "16", "20", "24", "28", "32","36","40","44"],
                        series: {{ Distance.distance_similar }}
                    }, {
                        high: 15,
                        low: 0,
                        showArea: true,
                        fullWidth: true,

                        axisY: {
                            onlyInteger: true,
                            offset: 20,
                            labelInterpolationFnc: function(value) {
                                return value / 1 + "k";
                            }
                        }
                    }
                );
                // ==============================================================
                // Trigger init of charts inside bootstrap tabs
                // ==============================================================

                $('a[data-toggle="pill"]').on("shown.bs.tab", function(event) {
                    $(".ct-chart").each(function(i, e) {
                        setTimeout(function() {
                            e.__chartist__.update();
                        }, 50);
                    });
                });
            });

        })(window, document, window.jQuery);