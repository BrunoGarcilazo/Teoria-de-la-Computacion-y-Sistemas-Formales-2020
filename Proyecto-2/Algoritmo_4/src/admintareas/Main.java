/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package admintareas;

import com.sun.org.apache.bcel.internal.generic.AALOAD;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.PriorityQueue;

/**
 *
 * @author Alvaro
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int dia = 14;
        int inc =0;
        ArrayList<Tarea> tareasDia = new ArrayList();
        Tarea p3 = new Tarea("pagar el alquiler",1,1);
        Tarea p4 = new Tarea("trabajar",1,6);
        Tarea p2 = new Tarea("pagar cuentas pendientes",2,2);
        Tarea p7 = new Tarea("estudiar", 2,2);
        Tarea p5 = new Tarea("sacar el perro",3,1);
        Tarea p6 = new Tarea("partido de Uruguay",3,2);
        Tarea p1 = new Tarea("salir a correr",3,1);
        Tarea p8 = new Tarea("ir al supermercado",4,1);
        Tarea p9 = new Tarea("arreglar la bicicleta",4,2);
        Tarea p10 = new Tarea("comprar ropa",4,1);
        Tarea p11 = new Tarea("comprar mueble",4,1);

        
    
        Tarea[] listaDeTareas = {p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11} ;
        
        HeapSort heap = new HeapSort();
        Tarea[] listaOrdenada =heap.ordenarPorHeapSort(listaDeTareas);
        
        while(dia>=0 && inc<listaDeTareas.length){
            if((dia-listaDeTareas[inc].getDuracion())>=0){
                tareasDia.add(listaDeTareas[inc]);
                dia= dia-listaDeTareas[inc].getDuracion();
            }
            inc++;
        }
        
        for (int i = 0; i < tareasDia.size(); i++) {
            System.out.println(tareasDia.get(i).getNombre());
            
        }        
    }
    
}
