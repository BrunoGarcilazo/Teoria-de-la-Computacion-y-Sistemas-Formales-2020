/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package admintareas;

/**
 *
 * @author Alvaro
 */
public class HeapSort {
    
    
    private void intercambiar(Tarea[] vector, int pos1, int pos2) {
		Tarea temp = vector[pos2];
		vector[pos2] = vector[pos1];
		vector[pos1] = temp;
	}
    
    
    public Tarea[] ordenarPorHeapSort(Tarea[] datosParaClasificar) {
        for (int i = (datosParaClasificar.length - 1) / 2; i >= 0; i--) { //Armo el heap inicial de n-1 div 2 hasta 0
            armaHeap(datosParaClasificar, i, datosParaClasificar.length - 1);
        }
        for (int i = datosParaClasificar.length - 1; i >= 1; i--) {
            intercambiar(datosParaClasificar, 0, i);
            armaHeap(datosParaClasificar, 0, i - 1);
        }
        return datosParaClasificar;
    }
    private void armaHeap(Tarea[] datosParaClasificar, int primero, int ultimo) {
        if (primero < ultimo) {
            int r = primero;
            while (r <= ultimo / 2) {
                if (ultimo == 2 * r) { //r tiene un hijo solo
                    if (datosParaClasificar[r].getPrioridad() < datosParaClasificar[r * 2].getPrioridad()) { //1er error
                        intercambiar(datosParaClasificar, r, 2 * r);
                        //r = 2 ;
                        r=2*r;
                        } else {
                         r = ultimo;
                    }
                   
                } else { //r tiene 2 hijos
                    int posicionIntercambio = 0;
                    if (datosParaClasificar[2 * r].getPrioridad() > datosParaClasificar[2 * r + 1].getPrioridad()) {
                        posicionIntercambio = 2 * r;
                    } else {
                        posicionIntercambio = 2 * r+1;
                    }
                    if (datosParaClasificar[r].getPrioridad() < datosParaClasificar[posicionIntercambio].getPrioridad()) {
                        intercambiar(datosParaClasificar, r, posicionIntercambio);
                        r = posicionIntercambio;
                    } else {
                        r = ultimo;
                    }
                }
            }
        }
    }
}
