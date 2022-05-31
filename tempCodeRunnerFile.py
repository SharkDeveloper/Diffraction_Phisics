for i in range(len(coordinates[0])-1,0,-3):
            series = QSplineSeries(self.plot)
            series.append(coordinates[1][i],-coordinates[0][i])
            series.append(coordinates[1][i-1],-coordinates[0][i-1])
            series.append(coordinates[1][i-2],-coordinates[0][i-2])
            
            self.plot.addSeries(series)